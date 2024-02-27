from django.shortcuts import render
from .models import *


# Create your views here.

def home (request):
    fielddatas = NodeFieldData.objects.all()
    fielddates = NodeFieldDate.objects.all()

    return render(request, 'sssa_home.html', {
        "fielddatas" : fielddatas,
        "fielddates" : fielddates,

    })


