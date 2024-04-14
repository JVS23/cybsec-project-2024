from django.db import models

from django.contrib.auth.models import User

class Item(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	note = models.TextField()
