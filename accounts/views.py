from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm, RegistrationForm
from accounts.models import User
from django.contrib import messages
# Create your views here.
@login_required
def dashboard(request):
    return render(request,'accounts/index.html')

@login_required
def profile(request):
	user = request.user
	form = UserForm(instance=user)
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
	return render(request,'accounts/profile.html',{'form':form})

def register(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			success = messages.success(request,f'Thank you for creating an account here ! please login !')		
	return render(request,'accounts/register.html', {'form':form})		