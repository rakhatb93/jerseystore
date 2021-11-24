from django.shortcuts import render
from .models import Sporttype


def index(request):
	return render(request, "store/index.html", {"sporttypes": Sporttype.objects.all()})

def football(request):
    return render(request, "store/football.html")

def basketball(request):
    return render(request, "store/basketball.html")

def hockey(request):
    return render(request, "store/hockey.html")

def epl(request):
    return render(request, "store/epl.html")

def laliga(request):
    return render(request, "store/laliga.html")

def ligueun(request):
    return render(request, "store/ligueun.html")

def bundesliga(request):
    return render(request, "store/bundesliga.html")

def seriea(request):
    return render(request, "store/seriea.html")

def nba(request):
    return render(request, "store/nba.html")

def euroleague(request):
    return render(request, "store/euroleague.html")

def nhl(request):
    return render(request, "store/nhl.html")

def khl(request):
    return render(request, "store/khl.html")