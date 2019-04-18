from django.shortcuts import render, redirect, get_object_or_404
from .forms import DataForm, OptionForm
from .models import Data, Option
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def add_data(request):
	form = DataForm()
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Data has been saved!')
			return redirect('add_data')
	return render(request, 'master_data/add_data.html',{'form':form})

@login_required
def data_list(request):
	data_list = Data.objects.all()
	paginator = Paginator(data_list,10)
	try:
		page = request.GET.get('page','1')
	except:
		page = 1
	try:
		datas = paginator.page(page)
	except(EmptyPage, InvalidPage):
		datas = paginator.page(paginator.num_pages)
	context = {
		'datas':datas
		}
	return render(request, 'master_data/data_list.html', context)

@login_required
def edit_data(request,pk):
	data = Data.objects.get(pk=pk)
	form = DataForm(instance=data)
	if request.method == 'POST':
		form = DataForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			messages.success(request,'Data has been updated !')
			return redirect('data_list')
	return render(request, 'master_data/add_data.html',{'form':form})

@login_required
def delete_data(request,pk):
    data = Data.objects.get(pk=pk)
    data.delete()
    return redirect('data_list')

@login_required
def option(request):
	form = OptionForm()
	option_list = Option.objects.all()
	paginator = Paginator(option_list,10)
	try:
		page = request.GET.get('page','1')
	except:
		page = 1
	try:
		options = paginator.page(page)
	except(EmptyPage, InvalidPage):
		options = paginator.page(paginator.num_pages)	
	if request.method == 'POST':
		form = OptionForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Option has been saved!')
			return redirect('option')
	context = {
		'form':form,
		'options':options
	}		
	return render(request, 'master_data/option.html', context)

@login_required
def edit_option(request,pk):
	data = Option.objects.get(pk=pk)
	form = OptionForm(instance=data)
	if request.method == 'POST':
		form = OptionForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			messages.success(request,'Option has been modified !')
			return redirect('option')
	return render(request,'master_data/option.html',{'form':form})	

@login_required
def delete_option(request,pk):
	data = Option.objects.get(pk=pk)
	data.delete()
	messages.success(request, 'Option has been deleted !')
	return redirect('option')