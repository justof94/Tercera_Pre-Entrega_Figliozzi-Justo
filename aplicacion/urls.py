from django.urls import path, include
from .views import *

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home/', home, name='home'),
    path('equiposRed/', equiposRed, name='equiposRed'),
    path('equiposTelecontrol/', equiposTelecontrol, name='equiposTelecontrol'),
    path('equiposProteccion/', equiposProteccion, name='equiposProteccion'),
]