 
from django.conf.urls import include, url
from . import views 

urlpatterns= [
		url(r'^$', views.portada,name="portada"),
		url(r'^app/$',views.apli_min,name="apli_min"),

	]