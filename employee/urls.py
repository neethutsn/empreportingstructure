from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.homepage,name='home'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('dashboard/',views.dashpage,name='dashboard'),
    path('viewemployees/',views.employeepage,name='viewemployees'),
    path('superdash/',views.supervisorpage,name='superdash'),
    path('logout/',views.logoutpage,name='logout'),

]