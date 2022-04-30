from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class custom_user(AbstractUser):
    number=models.CharField(max_length=12)

class profile(models.Model):
    user=models.OneToOneField(custom_user,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='images')