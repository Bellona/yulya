from django.shortcuts import render_to_response
from yulya.models import Painting

def home(request):
	pictures = Painting.objects.all().order_by('-created_date')[:10]
	# import pdb;pdb.set_trace()
	return render_to_response('main.html', {'pictures': pictures})

def aboutme(request):
	return render_to_response('aboutme.html')

def contacts(request):
	return render_to_response('contacts.html')