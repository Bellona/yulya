from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$', 'yulya.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^aboutme/', 'yulya.views.aboutme', name='aboutme'),
	url(r'^contacts/', 'yulya.views.contacts', name='contacts'),

	url(r'^admin/', include(admin.site.urls)),
)
