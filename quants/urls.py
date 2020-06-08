from .views import *
from django.urls import path

urlpatterns = [
    path('it/', showItQuant),
    path('vr-ar/', showVrQuant),
    path('chess/', showChessQuant),
    path('design/', showDesignQuant),
    path('hi-tech', showHiTechQuant),
    path('english/', showEnglishQuant),
    path('robo/', showRoboQuant),
    path('energy/', showEnergyQuant),
    path('math/', showMathQuant)
]