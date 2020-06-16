from django.db import models

# Create your models here.
class Status(models.Model):
    situation = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.situation

class Patiente(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    rg = models.IntegerField(null=True)
    cpf = models.IntegerField(null=True)
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=250, null=True)
    cpf = models.PositiveIntegerField()
    senha = models.CharField(max_length=250)


    def __str__(self):
        return self.name
