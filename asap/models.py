from django.db import models

# Create your models here.
class Asap_Upload(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	photo = models.FileField(null = True)

	def __str__(self):
		return(self.title)

