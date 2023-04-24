from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, Profileupdateform
from laundry.models import clothes
# Create your views here.

def register(request): 
    if request.method== 'POST':
        form= UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Now you can login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'user/register.html',{'form':form})

@login_required(login_url='login')
def profile(request):
    if request.method== 'POST': 
        p_form = Profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Profile updated successfully!')
            return redirect('profile')
    else:
        p_form = Profileupdateform(instance=request.user.profile)
    n_times = clothes.objects.filter(std=request.user)
    u_id = request.user.id
    number = {'times': n_times.count(), 'p_form': p_form, 'u_id': u_id} 
    return render(request,'user/profile.html',number)

    
