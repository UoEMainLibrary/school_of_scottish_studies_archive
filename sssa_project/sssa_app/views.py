from django.shortcuts import render

from .models import Alst, AlstTable



# Create your views here.

def home (request):
    return render(request, 'sssa_home.html')

def alst_table(request):
    tables = Alst.objects.all()

    return render(request, "alst_table.html", {
        "tables": tables
    })

