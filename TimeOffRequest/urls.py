"""
URL configuration for TimeOffRequest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import TimeOffRequestView

# TODO: update URLs to include home, form, and view request page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('time-off-request/', TimeOffRequestView.as_view(), name='time_off_request'),
    #add path for home page
    path('', HomeView.as_view(), name='home'),
    #add path for view request page
    path('view-request/', TimeOffRequestView.as_view(), name='view_request'),
]
