from django.db import models

class User(models.Model):
	"""
	This class contains the user login information ie username and password
	"""
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return self.username

class UserDetails(models.Model):
	"""
	This class contains all the personal and public information of the user ie name, email address, phone no, dob, hometown, etc
	"""
	uid = models.ForeignKey(User)
	name = models.CharField(max_length=50)
	dob = models.DateField(auto_now=False, auto_now_add=False)
	email = models.EmailField(max_length=254)
	hometown = models.CharField(max_length=50)
	course = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name