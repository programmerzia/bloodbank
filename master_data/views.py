from django.shortcuts import render, redirect, get_object_or_404
from .forms import DataForm, OptionForm
from .models import Data, Option
from django.contrib import messages

def add_data(request):
	form = DataForm()
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Data has been saved!')
			return redirect('add_data')
	return render(request, 'master_data/add_data.html',{'form':form})

def data_list(request):
    datas = Data.objects.all()
    context = {
    	'datas':datas
    }
    return render(request, 'master_data/data_list.html', context)

def edit_data(request,pk):
    form = Data.objects.get(pk=pk)
    if request.method == 'POST':
    	form = DataForm(request.POST,instance=form)
    	if form.is_valid():
    		form.save()
    		redirect('data_list')
    return render(request, 'master_data/add_data.html',{'form':form})		

def delete_data(request,pk):
    data = Data.get_object_or_404(pk=pk)
    data.delete()
    return redirect('data_list')

def option(request):
	form = OptionForm()
	options = Option.objects.all()
	context = {
		'form':form,
		'options':options
	}
	if request.method == 'POST':
		form = OptionForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Option has been saved!')
			return redirect('option')
	return render(request, 'master_data/option.html', {'form':form,'options':options})		
def edit_option(request,pk):
	return False
def delete_option(request):
	return False		