from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name','last_name','email','contact','city','state','zip_code','area','blood_group','photo']

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']