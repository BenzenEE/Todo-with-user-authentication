from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True,max_length=30)
    password = models.CharField(max_length=30)

class Tlist(models.Model):
    # status_choice = [
    #     ('C','COMPLETED'),
    #     ('P','PENDING'),
    # ]
    title = models.TextField(max_length=100)
    status = models.CharField(max_length=15, default='Pending')
    fok = models.ForeignKey(Test ,on_delete=models.CASCADE)