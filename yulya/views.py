from django.shortcuts import render_to_response

def home(request):
	return render_to_response('main.html')

def aboutme(request):
	return render_to_response('aboutme.html')

def contacts(request):
	return render_to_response('contacts.html')