from django.contrib import admin
from django.urls import path, include
from new import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('new/', include('new.urls')),

    
   
]