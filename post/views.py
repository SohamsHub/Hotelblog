from django.shortcuts import render
from post.models import Amenity , Listing , ListingPhoto , Reservation , Review
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def home(request):
    query = request.GET.get('q', '')
    listings = Listing.objects.select_related('host').prefetch_related('photos', 'reservations', 'reviews').order_by('-created_at')

    if query:
        listings = listings.filter(
            Q(title__icontains=query) |
            Q(address__icontains=query)
        )
        

    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    profile_id = None
    profile_pic = None
    if request.user.is_authenticated:
        try:
            user = User.objects.get(id=request.user.id)
            profile = user.profile
            profile_id = profile.id
            profile_pic = profile.profile_image
        except:
            profile_id = None
            profile_pic = None


    context =  {
        'listing': page_obj,
        'profile_id': profile_id,
        'profile_pic' : profile_pic,
    }

    return render(request, 'post/home.html', context)




def listing_room(request , id):
    listing_room = Listing.objects.select_related('host').prefetch_related('photos','reservations','reviews').get(id = id)

    context = {
        'listing_room' : listing_room , 
        }
    
    
    return render(request, 'post/listing_room.html', context)




