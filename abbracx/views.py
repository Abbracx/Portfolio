from django.shortcuts import render, get_object_or_404
from django.urls import reverse



# Create your views here.
def home_view(request):
	data = {
		'page': 'Homepage',
	}
	return render(request, 'abbracx/documents.home.html', data)