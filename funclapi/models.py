from django.db import models


class user(models.Model):
	uid = models.CharField(max_length=50, null=False)
	height = models.CharField(max_length=50, null=False)
	weight = models.CharField(max_length=50, null=False)
	age = models.CharField(max_length=50, null=False)
	gender = models.CharField(max_length=50, null=False)
	bmr = models.CharField(max_length=50, null=False)
	
	def _str_(self):
		return self.uid