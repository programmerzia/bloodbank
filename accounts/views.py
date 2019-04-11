from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm, RegistrationForm
from accounts.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
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
			success = messages.success(request,'Thank you for creating an account here ! please login !')		
			return redirect('login/')
	return render(request,'accounts/register.html', {'form':form})		

@login_required
def add_user(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			user, created = User.objects.get_or_create(username=username, email=email)
			if created:
				user.set_password(form.cleaned_data['password1'])
				user.save()
				messages.success(request,'User account has been created !')
				return redirect(request, 'accounts/add_user.html')
	return render(request, 'accounts/add_user.html', {'form':form})

@login_required
def list_user(request):
	user_list = User.objects.all().order_by('-id')
	paginator = Paginator(user_list,10)
	try:
		page = request.GET.get('page','1')
	except:
		page = 1
	try:
		users = paginator.page(page)
	except(EmptyPage, InvalidPage):
		users = paginator.page(paginator.num_pages)	
	context = {
		'users':users
	}
	
	return render(request, 'accounts/list_user.html', context)

@login_required
def add_member(request):
	return HttpResponse('add member here...')

@login_required
def list_member(request):
	return HttpResponse("list member here...")				