from django.shortcuts import render_to_response
from django.template import RequestContext
from yulya.models import Copy, Restoration, Blog, Comment
from yulya.forms import CommentForm
import datetime


def home(request):
	#pictures = Painting.objects.all().order_by('-created_date')[:10]
	# import pdb;pdb.set_trace()
	return render_to_response('main2.html')

def aboutus(request):
	return render_to_response('aboutus.html')