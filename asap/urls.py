from django.conf.urls import url
from .views import asap_form , asap_feed

urlpatterns = [
	url(r'^forms/$',asap_form,name='asap_upload'),
	url(r'^$',asap_feed,name ='asap_feed'),
	]

