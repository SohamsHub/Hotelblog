from django.contrib import admin
from .models import Amenity , Listing , ListingPhoto , Reservation , Review

# Register your models here.
admin.site.register(Amenity )
admin.site.register(Listing )
admin.site.register(ListingPhoto)
admin.site.register(Reservation )
admin.site.register(Review)