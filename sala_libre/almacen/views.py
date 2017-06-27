from django.shortcuts import render
from .models import Laboratorio
from .forms import AppForm
from django.utils import timezone
import datetime
from bs4 import BeautifulSoup
import requests
def portada(request):
	return render(request, 'almacen/home.html',{})

def apli_min(request):
	f=True
	labs=Laboratorio.objects.all().order_by('n')
	#print(request)
	if request.method == "POST":
		if "AHORA" in request.POST:
			#print("aja")
			x = datetime.datetime.now()
			dicdias = {'MONDAY':'1','TUESDAY':'2','WEDNESDAY':'3','THURSDAY':'4','FRIDAY':'5','SATURDAY':'6','SUNDAY':'7'}
			anho = x.year
			mes =  x.month
			dia= x.day
			fecha = datetime.date(anho, mes, dia)
			fdia=dicdias[fecha.strftime('%A').upper()]
			fhora=x.hour
			#fhora-=24
			#if fhora<0:
			#	fhora*=-1
			print(fdia,fhora,"click")
			labs=Laboratorio.objects.filter(dia=fdia)
			labs=labs.filter(hora=fhora)
			for lab in labs:
				print(lab.dia,lab.hora)
				if lab.libre:
					f=False
					#print("seeeee")
					return render(request, 'almacen/app.html',{'lab':lab,'f':f})
			n=True
			f=False
			return render(request, 'almacen/app.html',{'labs':labs,'f':f,'n':n})
		form = AppForm(request.POST)
		if form.is_valid():
			
			fdia=int(form.cleaned_data['dia'])
			fhora=int(form.cleaned_data['hora'])+6
			labs=Laboratorio.objects.filter(dia=fdia)
			labs=labs.filter(hora=fhora)
			print(fdia,fhora)
			for lab in labs:
				print(lab.dia,lab.hora)
				if lab.libre:
					f=False
					#print("aja")
					return render(request, 'almacen/app.html',{'lab':lab,'f':f})
			n=True
			f=False
			return render(request, 'almacen/app.html',{'labs':labs,'f':f,'n':n})
	else:
		form=AppForm()
	#labs=Laboratorio.objects.all().order_by('n')
	return render(request, 'almacen/app.html',{'f':f,'form':form})