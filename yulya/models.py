from django.db import models

# Create your models here.
class Painting(models.Model):
	name = models.CharField(max_length = 100)
	path_to_picture = models.CharField(max_length = 100)
	category = models.CharField(max_length = 100)
	created_date = models.DateField()

	def __unicode__(self):
		return self.name