from __future__ import division
from turtle import color
from unittest import result
from django.db.models import Q
import folium
import geocoder
import json

from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404



# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

#django.db.model all item need for use
from django.db.models import Avg, Max, Min, Count
from numpy import product

# all models and forms name add korar jonno * use kora jay
from .models import *
from .forms import *

#models and forms class ar name dity hoy
from .models import Useri
from .forms import StudentReg

#Poject ar jonno model and form name
from .models import Userform
from .forms import UserReg

from .models import Ownerform
from .forms import OwnerformReg

from .models import houserate
from .forms import houserateform

from .models import measurement
from .forms import mapform

from .models import map
from .forms import mapformagain

from .models import Location
from django.http import JsonResponse

from django.contrib import messages


#Item ar ownerformfill models name ase. kono form nai tai use hoy nai form name..ara imgall ar ownerformfill page ar
from .models import Item
from .models  import ownerformfill


#project ar jonno django thyk nea table, models, bellow all 
#from django.contrib.auth.forms import UserCreationForm nisilm..akhn nijer form create korsi django r under a
from django.contrib.auth.forms import UserCreationForm
#my forms name SignUp.page name signup

from .forms import Create
from django.contrib.auth.models import User


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout



def home(request):
    return HttpResponse("sadia")

# table create add and show    
def indexpage(request):
  if request.method=='POST':
      fm=StudentReg(request.POST)
      if fm.is_valid():
          nm=fm.cleaned_data['name'] 
          em=fm.cleaned_data['email'] 
          pw=fm.cleaned_data['password'] 
          reg=Useri(name=nm, email=em, password=pw)
          reg.save()
  else:
      fm=StudentReg()  

  stud= Useri.objects.all() 
  return render(request,"index.html", {'form':fm, 'stu':stud})  

# this is another tutorial page
def userform(request):
    ans=0
    try:
       if request.method=="POST":
        n1=int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        ans=n1+n2

    except:
        pass
    return render(request,"userform.html",  {'output':ans}) 

#top index page table show in this page    
def test(request):
    tes=Useri.objects.all()
    return render(request, "test.html", {'te':tes})    



#delete option create method for index page
def delete_data(request,id):
    if request.method == 'POST':
        pi=Useri.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


#delete option create method for test page
def delete_data(request,id):
    if request.method == 'POST':
        pi=Useri.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/test')

        



#update data from edit page,retrive and save
def update_data(request, id):
    if request.method == 'POST':
         pi=Useri.objects.get(pk=id)
         fm=StudentReg(request.POST, instance=pi)
         if fm.is_valid():
             fm.save()  

    else:
           pi=Useri.objects.get(pk=id)
           fm=StudentReg(instance=pi)
            
    return render(request, 'edit.html', {'form':fm})




#house page start final year project
def house(request):
    return render(request, 'house.html')


def houseform(request):
    if request.method == 'POST':
        hf= UserReg(request.POST)
    
        if hf.is_valid():
            
           
           hf.save()
           messages.success(request, 'Your Account create successfully!!')

 
    else:
        hf= UserReg()     
    return render(request, "houseform.html", {'formhf':hf})



def rental(request):

    #address=request.POST.get('address')

    if request.method=='POST':
        form=mapformagain(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/rental')
    else:
        form=mapformagain()


    #geocoder code
    address=map.objects.all().last()

    location=geocoder.osm(address)
    lat=location.lat
    lng=location.lng
    country=location.country

    #correct area na dily data ty add hobe na
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your location input is invalid')



    #create map for bangladesh lat,lng and location num ok

    m=folium.Map(location=[23.684994, 90.356331], zoom_start=4)

  

    folium.Marker([lat, lng], tooltip='click for more', icon=folium.Icon(color='green', icon='cloud'), popup="<strong>Bangladesh</strong>").add_to(m)

    #we can want to add 8 division marker map to our creat map
    folium.Marker(location=[24.903561,91.873611], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Sylhet</strong>").add_to(m)
    folium.Marker(location=[24.098379,90.328712], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Dhaka</strong>").add_to(m)
    #baki gula per day ty nity hobe
    folium.Marker(location=[24.376930,88.603073], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Rajshahi</strong>").add_to(m)
    folium.Marker(location=[22.841930,89.558060], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Khulna</strong>").add_to(m)
    folium.Marker(location=[22.700411,90.374992], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Barishal</strong>").add_to(m)
    folium.Marker(location=[22.330370,91.832626], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Chittagong</strong>").add_to(m)
    folium.Marker(location=[24.744221,90.403008], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Mymensingh</strong>").add_to(m)
    folium.Marker(location=[25.740580,89.261139], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Rangpur</strong>").add_to(m)


    m=m._repr_html_()
    context={
        'm':m,
        'form':form,
    }
        

    return render(request, 'rental.html', context)


def tes(request):               #test korar jonno create views and urls

    a=Ownerform.objects.all()# test koraer jonno
    b=ownerformfill.objects.all()
    c=Userform.objects.all()


#test for recommandation with if else condition and filter
    rating=houserate.objects.filter(info_rate=5)
    
    bb=ownerformfill.objects.filter(houserent=1600, bedroom=5)    #ok work

#ok work this owner variable by filter..group a
    owner=ownerformfill.objects.filter(houserent__range=["5000", "20000"], housesize__range=["1000","1500"]).order_by('houserent', 'housesize')
   
    
    d=houserate.objects.all()

#for search this q
    if 'q' in request.GET:
        q=request.GET['q']
        data= houserate.objects.filter(info_rate__icontains=q)


    context={
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'bb':bb,
        'rating':rating,
        
        'owner':owner,
        

        
    }                #test sob end, hoy nai result

    return render(request, 'tes.html', context ) 



def owner(request):
    
    if 'q' in request.GET:
        q=request.GET['q']
        data= Userform.objects.filter(code__icontains=q)

    else:
        data= Userform.objects.all()
    
    context={
        'data':data
    }

    return render(request, 'owner.html', context)



def search(request):

#this is for term function for auto complete search division


   
    if 'q' in request.GET:
        q=request.GET['q']
        data= ownerformfill.objects.filter(division__icontains=q)

    else:
        data= ownerformfill.objects.all()       
     

    context={
        'data':data,
       
        
        
    }    

    return render(request, 'search.html', context)    




#signup page and authentication..it not create me.django create
def signup(request):
   
    form=Create()
    
    if request.method == "POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your Account create successfully!!')
            
            return HttpResponseRedirect('/uselog/')

    context={'form':form}

    return render(request, 'signup.html', context)



#login page and authentication..not create me..django create

def uselog(request):

    #x=User.objects.all()         #here User is django nijer model name..ja ami use korbo edit ar jonno password
    
    if request.method == "POST":
    
        username=request.POST.get('username')
        password=request.POST.get('password') 

        user=authenticate(request, username=username, password=password)

        if user is not None:

            login(request,user)

            return redirect('/dhaka/') #.ata active hoise

        else:
            messages.info(request,'Username and password incorrect')

     
     
    context={}

    #x=User.objects.all()           #here User is django nijer model name..ja ami use korbo edit ar jonno passwor

    return render(request, 'uselog.html', context)



#house owner form fillup page..here all house details add database 

def ownerform(request):
     
    form=OwnerformReg()
    
    if request.method == "POST":
        form=OwnerformReg(request.POST) #..ata ansi form ar class thyk..

        
        if len(request.FILES)!=0 :      
         form.img=request.FILES['img']


        if form.is_valid():
            form.save()

            messages.success(request, 'Your house add!')
            
           # return HttpResponseRedirect('/rental/').ata active but messg ar jonno off korse

    context={'form':form}

    return render(request, 'ownerform.html', {'form':form})


    #add it 1.if len(request.FILES)!=0 : 2. form.img=request.FILES['img']


def fill(request):

    if request.method =="POST":
        po=ownerformfill()

        po.ownername = request.POST.get('ownername')
        po.email = request.POST.get('email')
        po.ownerpin = request.POST.get('ownerpin')
        po.housecategory = request.POST.get('housecategory')
        po.housename = request.POST.get('housename')
        po.houserent=request.POST.get('houserent')

        po.division = request.POST.get('division')
        po.district = request.POST.get('district')
        po.area = request.POST.get('area')
        po.housesize = request.POST.get('housesize')
        

        po.bedroom = request.POST.get('bedroom')
        po.dinning = request.POST.get('dinning')
        po.drawing = request.POST.get('drawing')
        po.bathroom = request.POST.get('bathroom')
        po.kitchen = request.POST.get('kitchen')
        po.balcony = request.POST.get('balcony')

        po.allinfo=request.POST.get('allinfo')
        po.location=request.POST.get('location')       

        if len(request.FILES) != 0:
            po.img=request.FILES['img']
    
        
        po.save()


    return render(request, 'fill.html')

def imgall(request):
    
    if request.method == "POST":
        prod = Item()
       
        prod.details = request.POST.get('details')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/house/')
  

    
    return render(request, 'imgall.html')




#search auto add
def auto(request):
    if request.is_ajax():
       q = request.GET.get('term', '')
       products = ownerformfill.objects.filter(division__icontains=q)
       results = []
       for rs in products:
        product_json = {}
        product_json = rs.division 
        results.append(product_json)
        data = json.dumps(results)
    else:
      data = 'fail'
      mimetype = 'application/json'
    return HttpResponse(data, mimetype)


#dhaka r image fetch
def dhaka(request):

    fe=ownerformfill.objects.all()  #filter or all same e ase

    #old search thyk search try
    #this is for term function for auto complete search division
   
    if request.method == 'GET':
        query = request.GET.get('query')
        if query!=None:
            fe = ownerformfill.objects.filter(district__icontains=query).order_by('houserent', 'housesize')
              
        else:
             fe=ownerformfill.objects.all().order_by('houserent')     
        

    context={'fe':fe,
              
              }

    return render(request, 'dhaka.html', context)


#dhaka info page for pk (primary key ar ja kiso ase) data
def info(request, pk):   #pk mane database ar primary key dekhabe just

    fe=ownerformfill.objects.get(id=pk)  #primary key(pk) ja oi key ar details dekhabe

    ratevariable=houserateform()        #amar rate ai product ar jonno create form name houserateform

    #canAdd for rate model ar check ar jonno koyta star use korse
    canAdd=True
    reviewcheck=houserate.objects.filter(infor_id=fe).count()   #ai fe ta info ar uporer fe k bujayse..it is user variable upore..r infor_id ta houserate model ar foreng variable thyk nea
    if reviewcheck>0:
        canAdd=False
    

    #fetch review and rate from houserate model in this primary key of ownerformfill model thyk.fe holo primary ownerformfill key ar variable
    reviewfetch=houserate.objects.filter(infor_id=fe)           #infor_id holo houserate ar forengkey.ja ownerformfill thyk nea

    
    #average rating  create
    avg_reviewfetch=houserate.objects.filter(infor_id=fe).aggregate(avg_rate=Avg('info_rate'))


    #success to fetch rating reviews objects===details..ok
    d=houserate.objects.all().order_by('info_rate')


    #check for rate value for recommandation
    if 'r' in request.GET:
        r=request.GET['r']
        rat=houserate.objects.filter(info_rate__icontains=r)
    else:
        rat=houserate.objects.all()   

    
    

    #ok work this owner variable by filter..group a
    owner=ownerformfill.objects.filter(houserent__range=["5000", "20000"], housesize__range=["1000","1500"]).order_by('houserent', 'housesize')



    context={'fe':fe,
              'ratevariable':ratevariable,
              'canAdd':canAdd,
              'reviewfetch':reviewfetch,
              'avg_reviewfetch':avg_reviewfetch,

              'd':d,     #try success for fetch rate value

              'rat':rat,  #how much rate need value for people see
              'owner':owner, #ok work this owner variable by filter..group a
             
              }        

    

    return render(request, 'info.html', context)





#rate and review url...ok
def save(request, pid):
    projuct=ownerformfill.objects.get(pk=pid)
    reve=houserate.objects.create(
        infor_id=projuct,
        info_review=request.POST['info_review'],
        info_rate=request.POST['info_rate'],

    )

    data={
        'info_review':request.POST['info_review'],
        'info_rate':request.POST['info_rate'],
    }

    #average rating  create
    avg_reviewfetch=houserate.objects.filter(infor_id=projuct).aggregate(avg_rate=Avg('info_rate'))

    

    #return JsonResponse({'bool':True, 'data':data, 'avg_reviewfetch':avg_reviewfetch})   #ai line code dily o right ..but success ar jjonno reviewok page create

    return HttpResponseRedirect('/reviewok')



def reviewok(request):

    return render(request, 'reviewok.html')   #only success ar jonno create kora review and rating k



def recomitem(request,pk):

   # re=houserate.objects.get(id=pk)
    #fe=ownerformfill.objects.get(id=pk)
    fe=ownerformfill.objects.get(id=pk)   #it is need..as like as info page ar moto..and for back page go(info.html)
    de=houserate.objects.all()            # ata just sobai k dekhay for loop ar maddhome

    context={
        'fe':fe,
        'de':de,
    }

    return render(request, 'recomitem.html', context)   


