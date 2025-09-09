from django.db import models

# Create your models here.
class Employees(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)

    def __str__(self):
        return self.name