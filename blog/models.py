from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
# Create your models here.

# user_status = User.is_superuser
# print("\n===============\n",user_status,"\n===============\n")

class Blog(models.Model):
    title = models.CharField(max_length=300)
    blog = models.TextField()
    author = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    superuser_status = models.CharField(max_length=50)
