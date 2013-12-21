from django.shortcuts import render_to_response
from yulya.models import Copy
from yulya.models import Restoration

def home(request):
	#pictures = Painting.objects.all().order_by('-created_date')[:10]
	# import pdb;pdb.set_trace()
	return render_to_response('main1.html')

def aboutme(request):
	return render_to_response('aboutme.html')

def contacts(request):
	return render_to_response('contacts.html')

def copies_landscapes(request):	
	copies = Copy.objects.filter(category = 'landscape')
	return render_to_response('copy_landscape.html', {'copies': copies})

def copies_stilllife(request):	
	copies = Copy.objects.filter(category = 'still_life')
	return render_to_response('copy_still_life.html', {'copies': copies})	

def restorations_icons(request):
	restorations = Restoration.objects.filter(category = 'icon')
	return render_to_response('restoration_icon.html', {'restorations': restorations})

def restorations_paintings(request):
	restorations = Restoration.objects.filter(category = 'painting')
	return render_to_response('restoration_painting.html', {'restorations': restorations})	