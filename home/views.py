from django.shortcuts import render, redirect
from .forms import SearchDonor
from accounts.models import Member
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