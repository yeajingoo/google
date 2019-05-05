from django.urls import path
from . import views

app_name = 'new'
urlpatterns = [
    path('signup/',  views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('log/', views.log, name='log'),
    path('create/', views.create, name="create"),
    path('home/', views.home, name="home"),
    path('show/<int:id>/', views.show, name="show"),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete/<int:id>', name)
    path('descript/', views.descript, name='descript'),
    path('mypage/',views.mypage, name="mypage"),
    path('save/',views.save,name="save"),
  ]