from django.contrib import admin
from django.urls import path,include
from . import views
app_name='todoapp'
urlpatterns = [

    path('',views.fun,name='fun'),
     path('delete/<int:id>/', views.delete, name='delete'),
     path('update/<int:id>/', views.update, name='update'),
    path('taskhome/',views.tasklist.as_view(),name='taskhome'),
    path('taskdetailss/<int:pk>/', views.taskdetail.as_view(), name='taskdetailss'),
    path('taskupdatee/<int:pk>/', views.taskupdate.as_view(), name='taskupdatee'),
    path('taskdeletee/<int:pk>/', views.taskdelete.as_view(), name='taskdeletee')

]
