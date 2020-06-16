from django.urls import path
from pacientes import views
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pacientes/home.html'), name='logout', kwargs={'next_page':'/'}),
]
