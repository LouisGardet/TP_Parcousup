# appParcoursup/admin.py

from django.contrib import admin
from .models import Ecole, Filiere, Candidat

admin.site.register(Ecole)
admin.site.register(Filiere)
admin.site.register(Candidat)