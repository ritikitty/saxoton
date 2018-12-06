from django.shortcuts import render, get_object_or_404

from .models import Gigs, FeaturedWorks

def home(request):
    gigs = Gigs.objects.all()
    featured = FeaturedWorks.objects.all()
    return render(request, 'home.html', {'gigs': gigs, 'featured':featured})

def gallerie(request):
    return render(request, 'gallerie.html',)
