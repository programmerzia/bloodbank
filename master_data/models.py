from django.db import models

class Option(models.Model):
	name = models.CharField(max_length=200,blank=True,null=True)
	status = models.BooleanField(default=True,null=True,blank=True)

	def __str__(self):
		return self.name

class Data(models.Model):
	option_id = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="option_list")
	option_name = models.CharField(max_length=200,blank=True, null=True)
	status = models.BooleanField(default=True,null=True,blank=True)

	def __str__(self):
		return self.option_name


