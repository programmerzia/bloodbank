from django.shortcuts import render

# Create your views here.
def add_data(request):
    return render(request, 'master_data/add_data.html',{'form':form})

def data_list(request):
    return False

def edit_data(request):
    return False

def delete_data(request,pk):
    return False