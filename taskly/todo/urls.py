from django.urls import path
from . import views





urlpatterns = [
    path('',views.index,name='index'),
    
    
    
    #--------------CRUD -  operations------------------#
 #-----------------------------------------------------#
    
    #CREATE TASK
    path('create-task/',views.createTask,name='create-task'),
    
    #READ TASK
    path('view_tasks/',views.viewTask,name='view_tasks'),
    
    #UPDATE TASK
    path('update-task/<str:pk>/',views.updateTask,name='update-task'),
    
    #DELETE TASK
    path('delete-task/<str:pk>/',views.deleteTask,name='delete-task'),
    
    
    
      #--------------REGISTER a user------------------# 
 #-----------------------------------------------------#
 
    
    path('register/',views.register,name='register'), 
    
    
    #--------------Login a user------------------# 
 #-----------------------------------------------------#
    
    path('my-login/',views.my_login,name='my_login'),
    
    
    
    #--------------Logout a user------------------# 
 #-----------------------------------------------------#
 
    path('logout-page/',views.logout_page,name='logout_page'),
    path('user-logout/',views.user_logout,name='user-logout')
 
]
