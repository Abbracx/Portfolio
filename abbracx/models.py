# Django import
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify

# python import
import random
import string
import uuid
# Create your models here.


def _random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


class Project(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	slug = models.SlugField()
	url = models.URLField(max_length=200)

	class Meta:
		verbose_name = "Blood Group"
		verbose_name_plural = verbose_name

	def unique_slug_generator(self, new_slug=None):
		if new_slug is not None:
			slug = new_slug
		else:
			slug = slugify(self.name)

		Klass = self.__class__
		qs_exists = Klass.objects.filter(slug=slug).exists()
		if qs_exists:
			new_slug = f'{slug}-{_random_string_generator(4)}'
			return self.unique_slug_generator(new_slug=new_slug)
		return slug

	def save(self, *args, **kwargs):
		self.slug = self.unique_slug_generator()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name
