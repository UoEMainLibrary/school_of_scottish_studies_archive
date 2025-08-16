"""
URL configuration for sssa_project project.

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
from django.urls import re_path as url
from sssa_app.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home, name='sssa_home'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('index/', index, name='index'),
    path('collections/', collections, name='collections'),
    path('people_and_place/', people_and_place, name='people_and_place'),
    path('subjects/', subjects, name='subjects'),
    path('listen_recordings/', listen_recordings, name='listen_recordings'),
    path('search_view/', search_view, name='search_view'),
    url('alst_create_record/', alst_create_record, name='alst_create_record'),
    url(r'^alst_details_record/(\d+)/', alst_details_record, name='alst_details_record'),
    path('alst_update_record/<int:id>/', alst_update_record, name='alst_update_record'),
    path('alst_delete_record/<int:id>/', alst_delete_record, name='alst_delete_record'),
    path('index/<str:word>/', filtered_items, name='filtered_items'),
]
