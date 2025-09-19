from django.shortcuts import get_object_or_404
from authy.models import Profile

def run():
    profile = Profile.objects.get(id = 1)
    print(profile.bio , profile.date_of_birth)

    

    