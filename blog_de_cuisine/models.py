from django.db import models
from django.conf import settings
from django.utils import timezone


class Publication(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    plat = models.ImageField(upload_to='assets/img/', blank=True, null=True)
    texte = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(blank=True, null=True)

    def publier(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titre