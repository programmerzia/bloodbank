from django import forms
from .models import Data, Option

class DataForm(forms.ModelForm):

	class Meta:
		model = Data
		fields = ['option_id','option_name','status']

class OptionForm(forms.ModelForm):
	
	class Meta:
		model = Option
		fields = ['name','status']