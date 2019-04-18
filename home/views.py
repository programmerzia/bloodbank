from django.shortcuts import render, redirect
from .forms import SearchDonor, ContactForm
from accounts.models import Member, User
from accounts.forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request, 'index.html')

def search_donor(request):
	form = SearchDonor()
	results = []
	if request.method == 'POST':
		form = SearchDonor(request.POST)
		if form.is_valid():
			city = form.cleaned_data['city']
			thana = form.cleaned_data['thana']
			area = form.cleaned_data['area']
			blood_group = form.cleaned_data['blood_group']
			results = Member.objects.all()
	context = {
		'form':form,
		'results':results
	}		
	return render(request, 'search_donor.html', context)

def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('thank-you')
	return render(request,'contact.html', {'form':form})

def thank_you(request):
	return render(request,'thank_you.html')

def register(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			user, created = User.objects.get_or_create(username=username,email=email)
			if created:
				user.set_password(password)
				user.save()
				messages.success(request,'Your account has been created successfully ! You can now login to your account !')
				return redirect('registration_success')
	return render(request,'register.html',{'form':form})

def registration_success(request):
	return render(request,'registration_success.html')