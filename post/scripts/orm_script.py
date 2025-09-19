from django.db import connection
from post.models import Amenity , Listing , ListingPhoto , Reservation , Review
from pprint import pprint
from django.contrib.auth.models import User


def run():
    # amenity = Amenity.objects.filter(name = Amenity.TypeChoices.AIR_CONDITIONING)
    # print(len(amenity))

    # listing = U.objects.filter(name = Amenity.TypeChoices.AIR_CONDITIONING)
    # user = User.objects.all()[1]
    # listing = user.listings.all()

    # print(user , listing)
    # listing = Listing.objects.all().order_by('-created_at')
    # print(listing)

    # listing = Listing.objects.select_related('host').prefetch_related('photos','reservations','reviews').all().order_by('-created_at')

    # for l in range(len(listing)):
    #     print(listing[l].reviews.all)

    # print(listing)

    # print(listing[1].reviews.all)
    # pprint(connection.queries)

    # ListingPhoto.objects.all().delete()

    listing_room = Listing.objects.select_related('host').prefetch_related('photos','reservations','reviews').filter(id = 3)
    print(listing_room)




    print(len(connection.queries))


    

    