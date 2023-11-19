from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import Person


# Create your views here.
def members(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def quiz1(request):
    template = loader.get_template('quiz1.html')
    return HttpResponse(template.render())

def quiz2(request):
    template = loader.get_template('quiz2.html')
    return HttpResponse(template.render())

def facts(request):
    template = loader.get_template('facts.html')
    return HttpResponse(template.render())

def belongingToACommunity(request):
    template = loader.get_template('belongingToACommunity.html')
    return HttpResponse(template.render())

def energyAndSustainability(request):
    template = loader.get_template('energyAndSustainability.html')
    return HttpResponse(template.render())
    
def financialLiteracy(request):
    template = loader.get_template('financialLiteracy.html')
    return HttpResponse(template.render())
    
def healthyRelationships(request):
    template = loader.get_template('healthyRelationships.html')
    return HttpResponse(template.render())
    
def keepingFit(request):
    template = loader.get_template('keepingFit.html')
    return HttpResponse(template.render())

def mentalHealthAndWellBeing(request):
    template = loader.get_template('mentalHealthAndWellBeing.html')
    return HttpResponse(template.render())
    
def rewards_eas(request):
    template = loader.get_template('rewards_eas.html')
    players = Person.objects.all()
    context = {"before" : 1, "after": 15, "players" : players} # we are taking in the before, after and the players database
    return HttpResponse(template.render(context, request))

def rewards_other(request):
    template = loader.get_template('rewards_other.html')
    players = Person.objects.all()
    context = {"before" : 1, "after": 15, "players" : players} # we are taking in the before, after and the players database
    return HttpResponse(template.render(context, request))