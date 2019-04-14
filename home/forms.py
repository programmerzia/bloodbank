from django import forms

class SearchDonor(forms.Form):
	city = forms.CharField(label='City', max_length=100)
	thana = forms.CharField(label='Thana', max_length=100)
	area = forms.CharField(label='Area', max_length=100)
	blood_group = forms.CharField(label='Blood Group', max_length=100)
