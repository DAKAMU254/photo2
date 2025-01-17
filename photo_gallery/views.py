from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Photo, UserProfile
from .forms import PhotoForm, UserProfileForm

# Photo Gallery Views
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo_gallery/photo_list.html', {'photos': photos})

def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'photo_detail.html', {'photo': photo})

@login_required
def photo_like(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)
    return redirect('photo_detail', photo_id=photo_id)

# User Registration View
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('photo_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('photo_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Profile View
@login_required
def user_profile(request):
    return render(request, 'profile.html')

# Edit User Profile View
@login_required
def profile_edit(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile_edit.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('photo_list')
    