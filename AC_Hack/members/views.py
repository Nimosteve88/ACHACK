from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def members(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def topics(request):
    template = loader.get_template('topics.html')
    return HttpResponse(template.render())

def rewards(request):
    template = loader.get_template('rewards.html')
    return HttpResponse(template.render())
