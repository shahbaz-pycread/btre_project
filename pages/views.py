from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import prices_choices, bedroom_choices, state_choices
# index views.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'prices_choices': prices_choices
    }
    return render(request, 'pages/index.html', context)
    

# about views.

def about(request):
    # Get all realtors.
    realtors = Realtor.objects.order_by('-hire_date')   

    # Get MVP.
    realtor_mvp = Realtor.objects.all().filter(is_mvp=True)
    
    context = { 
        'realtor_mvp' : realtor_mvp,
        'realtors' : realtors
    }
    return render(request, 'pages/about.html', context)


