from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

DIRECTION_CHOICES = (
    ('h', 'horizontal'),
    ('v', 'vertical'),	
)

COPY_CATEGORY_CHOICES = (
	('landscape', 'landscape'),
	('still_life', ' still_life'),
)
	
class Copy(models.Model):
	name = models.CharField(max_length = 100)
	author = models.CharField(max_length = 100)
	description = models.TextField()
	picture = models.ImageField(upload_to=".")
	category = models.CharField(max_length = 100, choices = COPY_CATEGORY_CHOICES)
	created_date = models.DateTimeField()
	direction = models.CharField(max_length = 1, choices = DIRECTION_CHOICES)

	def __unicode__(self):
		return self.name

RESTORATION_CATEGORY_CHOICES = (
	('icon', 'icon'),
	('painting', 'painting'),
)

class Restoration(models.Model):
	name = models.CharField(max_length = 100)
	author = models.CharField(max_length = 100)
	description = models.TextField()
	picture_before = models.ImageField(upload_to=".")
	picture_after = models.ImageField(upload_to=".")
	category = models.CharField(max_length = 100, choices = RESTORATION_CATEGORY_CHOICES)
	created_date = models.DateTimeField()
	direction = models.CharField(max_length = 1, choices = DIRECTION_CHOICES)

	def __unicode__(self):
		return self.name		

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	body = RichTextField()
	create = models.DateTimeField()
	tags = TaggableManager()

	def __unicode__(self):
		return self.title	
