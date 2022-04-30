from django.db import models
from users.models import custom_user
from django.utils import timezone
# Create your models here.
class post(models.Model):
    author=models.ForeignKey(custom_user,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images',blank=True)
    date_posted=models.DateTimeField(default=timezone.now)
class comment(models.Model):
    posts=models.ForeignKey(post,on_delete=models.CASCADE)
    author=models.ForeignKey(custom_user,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    image=models.ImageField(upload_to='comment_images',blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)