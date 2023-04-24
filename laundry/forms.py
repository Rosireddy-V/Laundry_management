from django import forms 
from .models import clothes, query

class Clothform(forms.ModelForm):
    class Meta: 
        model = clothes
        fields = ['Kurta','Pajama','Shirt','T_Shirt','Pant','Lower','Shorts','Bedsheet','Pillow_Cover','Towel','Dupatta','std']



class queryform(forms.ModelForm):
    class Meta: 
        model = query 
        fields = ['Laundry_id','Problem']