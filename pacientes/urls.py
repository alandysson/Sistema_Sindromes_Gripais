from django.urls import path
from pacientes import views
from django.contrib.auth.urls import views as auth_views

app_name = 'pacientes'

urlpatterns = [
    path('formulario/', views.PatientCreateView.as_view(), name='formulario'),
    path('lista/', views.PatientListView.as_view(), name='lista'),
]
