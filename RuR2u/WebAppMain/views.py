from django.shortcuts import render
from .models import Category
from .models import Elements


def index(request):
    cat = Category.objects.all()
    elem = Elements.objects.all()
    return render(request, 'index.html', {'cat': cat, 'elem': elem}) 


def pages(request, id):
    context = {'id': id, }
    page = Elements.objects.all()
    return render(request, 'page_detael.html', {'page': page, 'context': context})



