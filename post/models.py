from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models import Q 




# Create your models here.

def listing_directory_path(instances , filename):
    return 'listing_photo/listing_{0}/{1}'.format(instances.listing.id , filename)


class Amenity(models.Model):
    class TypeChoices(models.TextChoices):
        WIFI = 'wifi' , 'Wifi'
        KITCHEN = 'kitchen' , 'Kitchen'
        PRIVATE_ATTACHED_BATHROOM = 'private_attached_bathroom' , 'Private attached bathroom'
        WASHING_MACHINE = 'washing_machine' , 'Washing machine'
        DRYER = 'dryer' , 'Dryer'
        AIR_CONDITIONING = 'air_conditioning', 'Air conditioning'
        HEATING = 'heating' , 'Heating'
        DEDICATED_WORKSPACE = 'dedicated_workspace' , 'Dedicated workspace'
        TV = 'tv' , 'TV'
        HAIR_DRYER = 'hair_dryer' , 'Hair dryer'
        IRON = 'iron' , 'Iron'


    name = models.CharField(max_length = 100 , choices = TypeChoices.choices)
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name
    
    


class Listing(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=9, decimal_places=2)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    max_guests = models.PositiveIntegerField(default=1)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} listed by {self.host}"
    
    class Meta:
        constraints = [
            models.CheckConstraint (
                name = 'latitude_value_validation',
                check = Q(latitude__gte = -90 , latitude__lte = 90),
                violation_error_message = 'Latitude invalid: must fall between -90 and 90.'
            ) ,
            
            models.CheckConstraint (
                name = 'longitude_value_validation',
                check = Q(longitude__gte = -180 , longitude__lte = 180),
                violation_error_message = 'Longitude invalid: must fall between -180 and 180.'
            )
        
        ]
        
           


class ListingPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to= listing_directory_path , null = True,default='default.jpg')
    caption = models.CharField(max_length=255, blank=True , null = True)

    def __str__(self):
        return f"Image-{self.id}-{self.caption} for {self.listing.title}"
    

    
class Reservation(models.Model):
    class TypeChoices(models.TextChoices):
        PENDIND ='pending', 'Pending',
        CONFIRMED = 'confirmed', 'Confirmed',
        CANCELED = 'canceled', 'Canceled',
    
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reservations')
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=TypeChoices.choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Reservation by {self.guest.username} for {self.listing.title}"

  
    
class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()  # e.g., rating out of 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.listing.title}"
    
    class Meta:
        constraints = [
            models.CheckConstraint (
                name = 'rating_value_validation',
                check = Q(rating__gte = 1 , rating__lte = 5),
                violation_error_message = 'Rating invalid: must fall between 1 and 5.'
            )
        ]


