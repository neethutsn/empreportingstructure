from django.db import models

# Create your models here.

class User(models.Model):
    emp_name = models.TextField(max_length=50)
    emp_contact = models.TextField(max_length=20)
    emp_code = models.TextField(max_length=20)
    emp_cat = models.TextField(max_length=50)
    emp_pwd = models.TextField(max_length=50)
    emp_supervisor = models.TextField(max_length=50,null=True)
    