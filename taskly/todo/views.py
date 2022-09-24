from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

from .models import Task

from .forms import TaskForm,CreateUserForm,LoginForm

from django.contrib import messages 

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login

from django.contrib.auth.decorators import login_required

# Create your views here.

#home - index
def index(request):
    return render(request,"todo/index.html")



#CREATE TASKS:

def createTask(request):
    
    form = TaskForm()
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('view_tasks')
        
        
    
    context = {"form":form}
    
    return render(request,'todo/create-task.html',context=context)




#VIEW TASK

def viewTask(request):
    
    tasks = Task.objects.all()
    
    context = {"tasks":tasks}
    
    return render(request,'todo/view-tasks.html',context=context)



#UPDATE TASK
def updateTask(request,pk):
    
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance = task)
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST,instance=task)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('view_tasks')
    
    
    context = {"form":form}
    
    return render(request,'todo/update-task.html',context=context)
            
            
    
#DELETE TASK

def deleteTask(request,pk):
    
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        
        task.delete()
        
        return redirect('view_tasks')
    
    
    context = {'object':task}
    
    return render(request,'todo/delete-task.html',context=context)
    
    
    
    
    #Register / Creating a user
    
    
    
def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            
            messages.add_message(request, messages.INFO, 'hello welcome, Registered Successfully!\n Login here to join the community')
            
            return redirect('my_login')
        
    context = {'form':form}
    
    return render(request,'todo/register.html',context=context)

        
    
    # Login a user

def my_login(request):
    
    form = LoginForm
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request,  username = username , password = password)
            
            if user is not None:
                
                auth.login(request,user)
                
                messages.add_message(request, messages.INFO, 'welcome back, Login Successfully!')
                
                return redirect('/')

                
            
    context = {'form':form}
        
    return render(request,'todo/login.html',context=context)


    
    
    
    # Logout-page
@login_required(login_url='my_login')
def logout_page(request):
    
    return render(request,'todo/logout_page.html')



                
        
        # Logout a user

def user_logout(request):
    
    auth.logout(request)
        
    return redirect('/')
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    