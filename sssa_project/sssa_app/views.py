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

def alst_create_record(request):
    alst_record_form = AlstForm(request.POST or None)
    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('sssa_home')

    return render(request, 'forms/alst_record_form.html', {'alst_record_form': alst_record_form})


def alst_update_record(request, id):
    alst_update_record = Alst.objects.get(id=id)
    alst_record_form = AlstForm(request.POST or None, instance=alst_update_record)

    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('sssa_home')

    return render(request, 'forms/alst_record_form.html', {'alst_update_record': alst_update_record, 'alst_record_form': alst_record_form})