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
    # players is gonna be taken from a database of scores
    # TODO define the players document
    template = loader.get_template('rewards.html')
    players = [Player()]
    context = {'previous_score' : 1, 'final_score' : 2, 'players': players} # this has some dummy values atm to just see the result
    return HttpResponse(template.render(context, request))


# making a quick class for the player just to test
class Player():
    def __init__(self) -> None:
        self.rank = 1
        self.name = "Caspar"
        self.score = 1