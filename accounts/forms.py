from django import forms
from accounts.models import User, Member
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name','last_name','designation','email','contact','city','thana','zip_code','area','blood_group','photo']

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
class MemberForm(forms.ModelForm):
	
	class Meta:
		model = Member
		fields = ['name','contact','blood_group','area','city','thana','zip_code','photo']
		# widgets = {
		# 	'photo':forms.FileField(attrs={'required':False}),
		# }