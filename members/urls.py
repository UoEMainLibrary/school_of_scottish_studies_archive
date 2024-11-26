from django.urls import path
from members.views import *
from sssa_project.urls import *



urlpatterns = [
    path('login_user/', login_user, name='login'),
    path('logout_user/', logout_user, name='logout'),
    path('register_user/', register_user, name='register'),

]