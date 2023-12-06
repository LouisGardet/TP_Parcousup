from django.shortcuts import render
from .models import Ecole, Filiere, Candidat

def accueil(request):
    return render(request, 'index.html')

# appParcoursup/views.py (suite)
def consulter_offres(request):
    filieres = Filiere.objects.all()
    return render(request, 'consulter_offres.html', {'filieres': filieres})

def postuler(request, filiere_id):
    filiere = Filiere.objects.get(pk=filiere_id)
    return render(request, 'postuler.html', {'filiere': filiere})