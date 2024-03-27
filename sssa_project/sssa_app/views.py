from django.shortcuts import render, redirect
from .models import Alst, AlstTable
from .forms import *



# Create your views here.

def home (request):
    return render(request, 'sssa_home.html')

def alst_table(request):
    alst_records = Alst.objects.all()

    return render(request, "alst_table.html", {
        "alst_records": alst_records
    })

def alst_create_record(request):
    alst_record_form = AlstForm(request.POST or None)
    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('sssa_home')

    return render(request, 'forms/alst_record_form.html', {'alst_record_form': alst_record_form})


def alst_details_record(request, id):
    alst_records = Alst.objects.get(id=id)
    return render(request, 'forms/alst_details.html', {'alst_records': alst_records})






def alst_update_record(request, id):
    alst_record = Alst.objects.get(id=id)
    alst_record_form = AlstForm(request.POST or None, instance=alst_record)

    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('sssa_home')

    return render(request, 'forms/alst_record_form.html', {'alst_record': alst_record, 'alst_record_form': alst_record_form})