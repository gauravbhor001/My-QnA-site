"""
URL configuration for quora_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from qa.views import profile, home_redirect_view

urlpatterns = [
    path('', home_redirect_view, name='home'),  # Home URL that redirects to question list
    path('admin/', admin.site.urls),
    path('qa/', include('qa.urls')), # Include the main app's URLs
    path('accounts/profile/', profile, name='profile'),  # Profile page
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL


]
LOGIN_URL = '/accounts/login/'  # Path to the login page


