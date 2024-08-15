from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.publication_liste, name='publication_liste'),
    path('publication/<int:pk>/', views.publication_detail, name='publication_detail'),
    path('nouvelle/', views.nouvelle_publication, name='nouvelle_publication'),
    path('publication/<int:pk>/edit/', views.publication_modifier, name='modifier_publication'),
    path('publication/<int:pk>/delete/', views.publication_supprimer, name='supprimer_publication'),
    path('dashboard/', views.dashboard, name='dashboard'),
]