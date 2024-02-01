from django.shortcuts import render

# Create your views here.

from business.models import City, Category
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
