from django.shortcuts import render

def showItQuant(request):
	return render(request, 'quants/IT/index.html')

def showVrQuant(request):
	return render(request, 'quants/VR-AR/index.html')

def showChessQuant(request):
	return render(request, 'quants/Chess/index.html')

def showDesignQuant(request):
	return render(request, 'quants/Design/index.html')

def showHiTechQuant(request):
	return render(request, 'quants/Hi-Tech/index.html')

def showEnglishQuant(request):
	return render(request, 'quants/English/index.html')

def showRoboQuant(request):
	return render(request, 'quants/Robo/index.html')

def showEnergyQuant(request):
	return render(request, 'quants/Energy/index.html')

def showMathQuant(request):
	return render(request, 'quants/Math/index.html')