from django.conf.urls import patterns, include, url
from .views import IndexView, NombreView

urlpatterns = patterns('',
	
	url(r'^$', IndexView.as_view()),
	url(r'^nombre/', NombreView.as_view()),

)
