from django import forms
from .models import App

class AppForm(forms.Form):
	dia=forms.ChoiceField(widget = forms.Select(attrs={'class' : 'form-control'}),choices = ([('1','lu'), ('2','ma'),('3','mi'),('4','ju'), ('5','vi'),('6','sa'), ]),initial='1', required = True,)
	hora=forms.ChoiceField(widget = forms.Select(attrs={'class' : 'form-control'}),choices = ([('1','7am'), ('2','8am'),('3','9am'), ('4','10am'),('5','11am'),('6','12m'),('7','1pm'),('8','2pm'),('9','3pm'),('10','4pm'),('11','5pm'),('12','6pm'),]), initial='1',required = True,)

 			

 		