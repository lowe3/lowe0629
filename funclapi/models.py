from django.db import models


class user(models.Model):
	uid = models.CharField(max_length=50, null=False)
	height = models.CharField(max_length=50, null=False)
	weight = models.CharField(max_length=50, null=False)
	age = models.CharField(max_length=50, null=False)
	gender = models.CharField(max_length=50, null=False)
	bmr = models.CharField(max_length=50, null=False)

class seven(models.Model):
	items = models.CharField(max_length=50, null=False)
	calories = models.CharField(max_length=50, null=False)

class wefamily(models.Model):
	items = models.CharField(max_length=50, null=False)
	perserving = models.CharField(max_length=50)
	calories = models.CharField(max_length=50, null=False)
	protein = models.CharField(max_length=50)
	fat = models.CharField(max_length=50)
	saturatedfat = models.CharField(max_length=50)
	transfat = models.CharField(max_length=50)
	carbohydrate = models.CharField(max_length=50)
	sodium = models.CharField(max_length=50)
	sugar = models.CharField(max_length=50)