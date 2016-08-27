from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BlogPost(models.Model):
	author=models.CharField(max_length=25, null=True, blank=True)
	title=models.CharField(max_length=200)
	content=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	publish=models.BooleanField(default=False)


	def __str__(self):    # WORKS AS this function. defines inside a class so is diff from function def.
		return self.title
