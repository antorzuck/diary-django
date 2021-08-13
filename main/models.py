from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class memory(models.Model):
	content= models.TextField()
	date = models.DateField(("Date"), default=datetime.date.today)
	user= models.ForeignKey(User, on_delete=models.CASCADE,)