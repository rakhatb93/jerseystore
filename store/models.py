import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Sporttype(models.Model):
	title = models.CharField(max_length=25)
	description = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
		
	def was_published_recently(self):
	   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)	