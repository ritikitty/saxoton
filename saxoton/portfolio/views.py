from django.shortcuts import render, get_object_or_404

from .models import Gigs, FeaturedWorks, GalleryPicture

def home(request):
    gigs = Gigs.objects.all().order_by('Date')
    featured = FeaturedWorks.objects.all()
    return render(request, 'home.html', {'gigs': gigs, 'featured':featured})

def gallerie(request):
    items = GalleryPicture.objects.all()
    return render(request, 'gallerie.html', {'items': items})
