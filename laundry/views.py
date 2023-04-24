from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import clothe, clothes
from .forms import Clothform, queryform
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


'''laundry_history=[
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


]'''
# Create your views here.
@login_required(login_url='login')
def home(request):
    #return HttpResponse('<h1>Laundry Home</h1>')
    cloth_list = clothes.objects.filter(std=request.user).order_by('-Date') 
    page = request.GET.get('page',1)
    paginator = Paginator(cloth_list,2)

    try: 
        posts = paginator.page(page) 
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context={
        'hist': posts,'room_name': "broadcast"
    }
    paginate_by = 2 
    #context = ['-Date']
    return render(request,'laundry/home.html',context)

class clothlistview(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model=clothes 
    template_name = 'laundry/home.html'
    def get_queryset(self):
        qs = self.user
        return clothes.objects.filter(std=qs)
    
    context_object_name = 'hist'
    ordering = ['-Date']
    paginate_by = 3
    def test_func(self):
        cloth = self.get_object()
        if self.request.user == cloth.user:
            return True
        return False


class clothdetailview(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = clothes     
    def test_func(self):
        cloth = self.get_object()
        if self.request.user == cloth.std:
            return True
        return False

                                               #<app>/<model>_<viewtype>.html

@login_required(login_url='login')
def about(request,pk):
    #return HttpResponse('<h1>Laundry-About</h1>')
    list = []
    list = clothes.objects.filter(std=request.user)
    context = {
        'histo': clothes.objects.filter(std=request.user).get(id=pk)
    }
    return render(request,'laundry/about.html',context) 

@login_required(login_url='login')
def add_cloth(request): 
    if request.method== 'POST':
        form= Clothform(request.POST) 
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('std')
            messages.success(request, f'laundry added for {username}!')
            return redirect('addcloth')
    else:
        form=Clothform()
    return render(request,'laundry/add_cloth.html',{'form':form})

@login_required(login_url='login')
def laundry_query(request): 
    if request.method== 'POST':
        form= queryform(request.POST) 
        if form.is_valid():
            form.save()
            #username= form.cleaned_data.get('cloth')
            messages.success(request, f'query posted successfully!')
            return redirect('home')
    else:
        form=queryform()
    return render(request,'laundry/laundry_query.html',{'form':form})