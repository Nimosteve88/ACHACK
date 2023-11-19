from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from models import Person
import requests


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
    api_key = 'b2c8adec9244439385335aee2daf292e'
    url = 'https://newsapi.org/v2/everything'

    # Parameters for the News API request
    params = {
        'q': 'technology',
        'apiKey': api_key,
    }

    # Make the News API request
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])

    # Limit the number of articles to 8
    articles = articles[:8]

    # Pass the articles to the template
    context = {'articles': articles}
    return render(request, 'energyAndSustainability.html', context)
    
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
    api_key = 'b2c8adec9244439385335aee2daf292e'
    url = 'https://newsapi.org/v2/everything'

    # Parameters for the News API request
    params = {
        'q': 'health',
        'apiKey': api_key,
    }

    # Make the News API request
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    articles = articles[:8]

    # Pass the articles to the template
    context = {'articles': articles}
    return render(request, 'mentalHealthAndWellBeing.html', context)
    
def rewards_eas(request):
    template = loader.get_template('rewards_eas.html')
    players = [Person("You", "", 8), Person("Olatunde", "Bayo", 6), Person("Kwasi", "Appiah", 5), Person("Nancy", "Smith", 3), Person("Salmah", "Khan", 2)]
    context = {"before" : 4, "after": 8, "players" : players} # we are taking in the before, after and the players database
    return HttpResponse(template.render(context, request))

def rewards_other(request):
    template = loader.get_template('rewards_other.html')
    players = [Person("You", "", 7), Person("Olatunde", "Bayo", 5), Person("Kwasi", "Appiah", 4), Person("Nancy", "Smith", 2)]
    context = {"before" : 1, "after": 15, "players" : players} # we are taking in the before, after and the players database
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

class Person():
    def __init__(self, fname, lname, score):
        self.fname = fname
        self.lname = lname
        self.score = score

    def __str__(self) -> str:
        return self.fname + ' ' + self.lname