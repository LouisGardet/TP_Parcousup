# parcoursup/models.py
from django.db import models

class Ecole(models.Model):
    nom = models.CharField(max_length=100)

class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    choix = models.ManyToManyField(Filiere)
