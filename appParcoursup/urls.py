from django.urls import path
from .views import accueil, consulter_offres, postuler

urlpatterns = [
    path('', accueil, name='accueil'),
    path('consulter_offres/', consulter_offres, name='consulter_offres'),
    path('postuler/<int:filiere_id>/', postuler, name='postuler'),
]