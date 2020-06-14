from django.db import models
# from django.utils.safestring import mark_safe
# from django.template.defaultfilters import truncatechars

#   models here.


# Information Model

class Information(models.Model):
		name = models.CharField(max_length =100, verbose_name = "Your name")		
		quotes = models.TextField(verbose_name ="Your quotes")

		def __str__(self):
			return self.name


# About Model

class About(models.Model):
	short_description = models.TextField()
	description = models.TextField()
	image = models.ImageField(upload_to="about")


	# def admin_photo(self):
	# 	return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
	# 	admin_photo.short_description ='Image'
	# 	admin_photo.allow_tags = True


	class Meta:
		verbose_name = "About me"
		verbose_name_plural = "About me"

		def __str__(self):
			return self.short_description



#Service Model
			
class Service(models.Model):
		name = models.CharField(max_length =100, verbose_name = "Service name")		
		description = models.TextField(verbose_name ="About service")

		def __str__(self):
			return self.name


#Recent Work Model

class RecentWork(models.Model):
	tittle = models.CharField(max_length = 100, verbose_name = "Work tittle")
	image = models.ImageField(upload_to = "works")

	def __str__(self):
		return self.tittle


#Clients Model
class Client(models.Model):
	name = models.CharField(max_length = 100, verbose_name = "Client name")
	description = models.TextField(verbose_name = "Client say")
	image = models.ImageField(upload_to = "clients",default = "default.png")

	def __str__(self):
		return self.tittle



#
