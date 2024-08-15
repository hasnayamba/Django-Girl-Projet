from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publication 
from .forms import PublicationForm

def publication_liste(request):
    publications = Publication.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date')
    return render(request, 'blog_de_cuisine/publication_liste.html', {'publications': publications})


def publication_detail(request, pk):
    publication = get_object_or_404(Publication,pk=pk)
    return render(request, 'blog_de_cuisine/publication_detail.html',{'publication':publication})


def nouvelle_publication(request):
    if request.method == 'POST': 
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.auteur = request.user  
            publication.publication_date = timezone.now()
            publication.save()
            return redirect('publication_detail', pk=publication.pk)  
    else:
        form = PublicationForm()
    return render(request, 'blog_de_cuisine/nouvelle_publication.html', {'form': form})

def publication_modifier(request, pk):
    publ = get_object_or_404(Publication, pk=pk)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=publ)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.auteur = request.user  
            publication.publication_date = timezone.now()
            publication.save()
            return redirect('publication_detail', pk=pk)  
    else:
        form = PublicationForm(instance=publ)
    return render(request, 'blog_de_cuisine/modifier_publication.html', {'form': form})

def publication_supprimer(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('dashboard')
    return render(request, 'blog_de_cuisine/supprimer_publication.html', {'publication': publication})


def dashboard(request):
    publications = Publication.objects.all().order_by('-publication_date')
    return render(request, 'blog_de_cuisine/dashboard.html', {'publications': publications})
