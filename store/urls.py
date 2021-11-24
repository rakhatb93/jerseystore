from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('football/', views.football, name='football'),
   path('basketball/', views.basketball, name='basketball'),
   path('hockey/', views.hockey, name='hockey'),
   path('epl/', views.epl, name='epl'),
   path('laliga/', views.laliga, name='laliga'),
   path('ligueun/', views.ligueun, name='ligueun'),
   path('bundesliga/', views.bundesliga, name='bundesliga'),
   path('epl/', views.seriea, name='seriea'),
   path('nba/', views.nba, name='nba'),
   path('euroleague/', views.euroleague, name='euroleague'),
   path('nhl/', views.nhl, name='nhl'),
   path('khl/', views.khl, name='khl'),
]