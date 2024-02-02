from django.shortcuts import render
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

from business.models import City, Category,Company,Images
from home.models import Setting


def index(request):
    #category = categoryTree(0,'',currentlang)
    city = City.objects.all()
    category = Category.objects.all()
    setting = Setting.objects.all().order_by('-id')[0:1]

    context={
        'category':category,
        'city':city,        
        'setting':setting,        
    }
    return render(request, 'index.html',context)



def company(request): 
    #category = categoryTree(0,'',currentlang)
    city = City.objects.all()
    company = Company.objects.all()
    category = Category.objects.all()
    setting = Setting.objects.all().order_by('-id')[0:1]


    
    context = {
        'city': city,
        'category': category,
        'setting': setting,
        'company': company,

    }
       
    return render(request, 'main/list_company.html',context)

def company_detail(request,slug): 
    
    #category = categoryTree(0,'',currentlang)
    company = Company.objects.filter(slug = slug)
    city = City.objects.all()

    setting = Setting.objects.all().order_by('-id')[0:1]
    
    context = {
        'city': city,
        'setting': setting,
        'company': company,

    }    
    return render(request, 'main/company_detail.html',context)


