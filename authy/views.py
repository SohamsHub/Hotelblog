from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile
from django.contrib import messages
from authy.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def profiles(request, id):
    profile = get_object_or_404(Profile , id = id)

    authenticated = False
    if profile.user.id == request.user.id:
        authenticated = True

    context = {
        'profile' : profile,
        'authenticated':authenticated,
    }

    return render(request, 'authy/profile.html', context)


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('authy:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('authy:register')

        user = User.objects.create_user(username=username, password=password)
        profile = Profile.objects.create(user=user)
        login(request, user)
        return redirect('post:home')  
    
    return render(request, 'authy/register.html')
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post:home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'authy/login.html')


def logout_view(request):
    logout(request)
    return redirect('post:home')


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)


    if request.method == 'POST':
        profile.bio = request.POST.get('bio')
        profile.date_of_birth = request.POST.get('date_of_birth')
        profile.phone_no = request.POST.get('phone_no')
        profile.address = request.POST.get('address')
        profile.email_field = request.POST.get('email_field')
        profile.gender = request.POST.get('gender')

        if request.FILES.get('profile_image'):
            profile.profile_image = request.FILES['profile_image']

        profile.save()
        return redirect('authy:profiles', id=profile.id)

    return render(request, 'authy/editprofile.html', {'profile': profile})