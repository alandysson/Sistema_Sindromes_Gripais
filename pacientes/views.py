from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from pacientes.models import Patiente, Employee
from pacientes.forms import PatienteForm
from django.urls import reverse_lazy
# Create your views here.
class Home(TemplateView):
    template_name = 'pacientes/home.html'

class PatientCreateView(CreateView):
    model = Patiente
    form_class = PatienteForm
    success_url = reverse_lazy('home')
    template_name = 'pacientes/formulario.html'

class PatientListView(ListView):
    context_object_name = 'patients'
    model = Patiente
