from django.shortcuts import render
from django.http import HttpResponse


laundry_history=[
    {
        'Date':'20-2-2023',
        'Kurta':"none",
        'Pajama':"none",
        'Shirt':'1',
        'T_Shirt':'4',
        'Pant':'none',
        'Lower':'none',
        'Shorts':'4',
        'Bedsheet':'none',
        'Pillow_Cover':'none',
        'Towel':'1',
        'Dupatta':'none'
    },
    {
        'Date':'18-2-2023',
        'Kurta':"2",
        'Pajama':"1",
        'Shirt':'1',
        'T_Shirt':'2',
        'Pant':'1',
        'Lower':'none',
        'Shorts':'2',
        'Bedsheet':'none',
        'Pillow_Cover':'none',
        'Towel':'1',
        'Dupatta':'none'
    }


]
# Create your views here.
def home(request):
    #return HttpResponse('<h1>Laundry Home</h1>')
    context={
        'history':laundry_history
    }
    return render(request,'laundry/home.html',context)

def about(request):
    #return HttpResponse('<h1>Laundry-About</h1>')
    return render(request,'laundry/about.html',{'title': 'About'})
