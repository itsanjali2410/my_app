from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

def members(response):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
# Create your views here.
