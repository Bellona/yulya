from django.shortcuts import render_to_response
from django.template import RequestContext
from yulya.models import Copy, Restoration, Blog, Comment
from yulya.forms import CommentForm
import datetime


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

def blogs(request):
	blogs = Blog.objects.all().order_by('-create')
	return render_to_response('blog.html', {'blogs': blogs})


def post(request, pk):
	post = Blog.objects.get(id=int(pk))
	form = CommentForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		new_comment = Comment(
			author=form.cleaned_data['author'],
			body=form.cleaned_data['comment'],
			created=datetime.datetime.now(),
			Article_id=int(pk))
		new_comment.save()
		form = CommentForm()

	comment = Comment.objects.filter(Article=int(pk)).order_by('created')
	return render_to_response(
		'post.html', 
		{'post': post, 'comment': comment, 'form': form},
		context_instance=RequestContext(request))
