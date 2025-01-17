from django import forms
from .models import UserProfile, Photo

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'tags', 'image']
class PhotoUploadForm(forms.ModelForm):
    class Meta: 
        model = Photo    
        fields = ['title', 'description', 'image']
