from django.db import models
class user(models.Model):
	uid = models.CharField(max_length=100, null=False)
	height = models.CharField(max_length=100, null=False)
	weight = models.CharField(max_length=100, null=False)
	age = models.CharField(max_length=100, null=False)
	gender = models.CharField(max_length=100, null=False)
	bmr = models.CharField(max_length=100, null=False)
	tdee = models.CharField(max_length=100, null=True)

	def _str_(self):
		return self.uid

class seven(models.Model):
	items = models.CharField(max_length=100, null=False)
	calories = models.CharField(max_length=100, null=False)
	picture = models.CharField(max_length=250, null=True)

class wefamily(models.Model):
	items = models.CharField(max_length=100, null=False)
	perserving = models.CharField(max_length=100)
	calories = models.CharField(max_length=100, null=False)
	protein = models.CharField(max_length=100)
	fat = models.CharField(max_length=100)
	saturatedfat = models.CharField(max_length=100)
	transfat = models.CharField(max_length=100)
	carbohydrate = models.CharField(max_length=100)
	sodium = models.CharField(max_length=100)
	sugar = models.CharField(max_length=100)
	picture = models.CharField(max_length=250, null=True)

