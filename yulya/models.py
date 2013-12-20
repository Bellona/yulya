from django.db import models
from django.conf import settings


class Painting(models.Model):
	name = models.CharField(max_length = 100)
	picture = models.ImageField(upload_to=".")
	category = models.CharField(max_length = 100)
	created_date = models.DateTimeField()
	direction = models.CharField(max_length = 1)

	def __unicode__(self):
		return self.name