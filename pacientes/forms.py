from django import forms
from pacientes.models import Patiente, Employee

class PatienteForm(forms.ModelForm):
    class Meta():
        model = Patiente
        fields = ('name', 'age', 'cpf', 'rg', 'address', 'city', 'status')


# class EmployeeForm(forms.ModelForm):
#     class Meta():
#         model = Employee
#         fields = ('cpf', 'senha')
