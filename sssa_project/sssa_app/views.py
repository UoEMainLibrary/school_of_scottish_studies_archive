from django.shortcuts import render, redirect
from .models import Alst, AlstTable
from .forms import *



# Create your views here.

def home (request):
    return render(request, 'sssa_home.html')

def alst_table(request):
    tables = Alst.objects.all()

    return render(request, "alst_table.html", {
        "tables": tables
    })

def create_record(request):
    record_form = AlstForm(request.POST or None)
    if record_form.is_valid():
        record_form.save()
        return redirect('sssa_home')

    return render(request, 'forms/record_form.html', {'record_form': record_form})

