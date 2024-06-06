from django.urls import path
from members.views import *
from sssa_project.urls import *



urlpatterns = [
    path('login_user/', login_user, name='login'),

]