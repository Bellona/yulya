from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$', 'yulya.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^aboutme/', 'yulya.views.aboutme', name='aboutme'),
	url(r'^contacts/', 'yulya.views.contacts', name='contacts'),
	url(r'^copies_landscapes/', 'yulya.views.copies_landscapes', name='copies_landscapes'),
	url(r'^copies_stilllife/', 'yulya.views.copies_stilllife', name='copies_stilllife'),
	url(r'^restorations_icons/', 'yulya.views.restorations_icons', name='restorations_icons'),
	url(r'^restorations_paintings/', 'yulya.views.restorations_paintings', name='restorations_paintings'),

	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)