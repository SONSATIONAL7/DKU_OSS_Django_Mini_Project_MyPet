""" from django import forms
from .models import myPetText

class pet_form(forms.ModelForm):
    
    class Meta:
        model = myPetText
        fileds = '__all__'
     """