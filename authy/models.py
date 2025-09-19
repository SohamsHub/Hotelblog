from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Length
from post.models import Listing
from django.db.models import Q 

# Create your models here.

def profile_directory_path(instances , filename):
    return 'profiles/profile_{0}/{1}'.format(instances.user.username , filename)



class Profile(models.Model):
    
    class TypeChoices(models.TextChoices):
        MALE = 'male' , 'Male'
        FEMALE = 'female' , 'Female'
        OTHERS = 'others' , 'Others'

    user = models.OneToOneField(User, on_delete=models.CASCADE ,unique = True, related_name = 'profile')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None ,related_name = 'profiles')
    bio = models.TextField(blank = True , null= True)
    date_of_birth = models.DateField(blank = True , null= True )
    profile_image = models.ImageField(upload_to = profile_directory_path , blank = True , null= True)
    phone_no = models.CharField(max_length= 10,blank = True)
    address = models.CharField(max_length= 256 ,blank = True)
    email_field = models.EmailField(max_length=50 ,blank = True)
    gender = models.CharField(max_length = 10 , choices = TypeChoices.choices)  
    co_hosts = models.ForeignKey('self', blank=True, null= True, on_delete=models.CASCADE, related_name='co_hosted_by')



    def _str_(self):
        return self.user.username


    class Meta:
        constraints = [
            models.CheckConstraint(
                name = 'email_field_validation',
                check = Q(email_field__endswith = '@gmail.com'),
                violation_error_message = 'enter valid email id !',
            )
        ]