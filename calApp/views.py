from django.shortcuts import render , redirect 
import os
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')


def delete(request,id):
    prof=profile.objects.get(id=id)
    if prof.image != 'def.png':
        os.remove(prof.image.path)
    prof.delete()
    return redirect('data')

def data(request):
    prof=profile.objects.all()
    return render(request,'data.html',locals())


def create(request):
    if request.method == "POST":
        name=request.POST.get('name')
        mail=request.POST.get('email')
        number=request.POST.get('num')
        image=request.FILES.get('img')
        adrs = request.POST.get('address')
        gender=request.POST.get('gender')
        relagion=request.POST.get('relagion')
        print(name)
        if image:
            prof = profile.objects.create(name=name, email=mail, number=number, image=image,Adress=adrs,gender=gender,relagion=relagion)
            prof.save()
            return redirect('index')
        else:
            prof=profile.objects.create(name=name,email=mail,number=number,Adress=adrs,gender=gender,relagion= relagion)
            prof.save()
            return redirect('index')
    
    return render(request,'create.html')
