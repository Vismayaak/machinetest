from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    date_of_join=models.DateField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='image/',null=True)

