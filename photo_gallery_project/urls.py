"""
URL configuration for photo_gallery_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin
    path('photo_gallery/', include('photo_gallery.urls')),  # Include the photo_gallery app URLs

    # Redirect the root URL to the photo gallery's home page
    path('', include('photo_gallery.urls')),  # Root URL redirects to the app's main page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
