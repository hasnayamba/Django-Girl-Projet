from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['titre', 'texte', 'publication_date', 'plat']

        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control custom-input', 
                'placeholder': 'Entrer le titre',
                'style': 'background-color: #f9f9f9; border-radius: 5px; padding: 20px;'
            }),
            'texte': forms.Textarea(attrs={
                'class': 'form-control custom-textarea', 
                'placeholder': 'Décrivez le plat',
                'style': 'background-color: #f9f9f9; border-radius: 5px; padding: 10px; min-height: 150px;'
            }),
            'publication_date': forms.TextInput(attrs={
                'class': 'form-control custom-date', 
                'type': 'date',
                'style': 'background-color: #f9f9f9; border-radius: 5px; padding: 20px;'
            }),
            'plat': forms.ClearableFileInput(attrs={
                'class': 'form-control custom-file-input', 
                'style': 'padding: 20px;'
            }),
        }