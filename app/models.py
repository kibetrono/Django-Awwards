from django.db import models
import datetime as dt

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank="True")
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = CloudinaryField("image")
    url = models.URLField(blank=True)
    location = models.CharField(max_length=100, default="Nairobi")
    date = models.DateTimeField(auto_now_add=True, null=True)

  