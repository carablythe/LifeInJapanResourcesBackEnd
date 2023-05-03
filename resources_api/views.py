from django.shortcuts import render
from django.http import HttpResponse

from . models import Resource
from . models import Forum 

def home(request): 

    resources = Resource.objects.all()

    context = {'resources': resources}

    
    return render(request,'resources_api/index.html', context=context)


