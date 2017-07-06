from django.shortcuts import render
from .models import Laboratorio
from .forms import AppForm
from django.utils import timezone
import datetime
from bs4 import BeautifulSoup

import requests

def minero():

	from bs4 import BeautifulSoup
	import requests

	URL_BASE = "http://labcomp.unet.edu.ve/horario.php?id="
	MAX_PAGES = 11

	counter = 0
	lab=0
	print("andres")
	for i in range(1, MAX_PAGES):
	    lab+=1
	    if lab==5:
	    	lab+=1
	    # Construyo la URL
	    if i > 1:
	        url = URL_BASE+str(i)
	    else:
	        url = URL_BASE+str(1)
	    print(url)
	    # Realizamos la petición a la web
	    req = requests.get(url)
	    # Comprobamos que la petición nos devuelve un Status Code = 200
	    statusCode = req.status_code
	    if statusCode == 200:

	        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
	        html = BeautifulSoup(req.text, "html.parser")

	        # Obtenemos todos los divs donde estan las entradas
	        entradas = html.find_all('tr')
	        s=0
	        # Recorremos todas las entradas para extraer el título, autor y fecha
	        
	        h=7
	        for entrada in entradas:
	            
	            titulo = entrada.find_all('td')
	            hora=0
	            counter=0
	            for t in titulo:
	            	counter += 1
	            	x=t.getText()
	            	if x == '7am-8am':
	            		s=1
	            	if s:
	            		hora+=1
	            		
	            		if len(x)==1:
	            			print('lab',lab,'dia',counter-1,'hora',h,True,x)
	            			labs=Laboratorio.objects.create(n=lab,dia=counter-1,hora=h,libre=True,clases=x)
	            		else:
	            			if len(x)>=10:
	            				labs=Laboratorio.objects.create(n=lab,dia=counter-1,hora=h,libre=False,clases=x)
	            				print('lab',lab,'dia',counter-1,'hora',h,False,x)
	            		if hora==7:
	            			h+=1
	            			hora=0

	            		# labs=Laboratorio.objects.create(n=lab,dia=counter-16,hora=7,libre=False,clases=x)

	            	if x == '6pm-7pm':
	            		s=0

	    else:
	        # Si ya no existe la página y me da un 400
	        break
 

def portada(request):
	minero()
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