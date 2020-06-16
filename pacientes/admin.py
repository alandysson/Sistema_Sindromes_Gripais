from django.contrib import admin
from pacientes.models import Patiente, Status, Employee
# Register your models here.
admin.site.register(Status)
admin.site.register(Patiente)
admin.site.register(Employee)
