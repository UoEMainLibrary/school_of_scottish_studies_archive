from django.shortcuts import render, redirect
from .models import Alst, AlstTable
from .forms import AlstForm
from django.db.models import Q

    #alst_records = Alst.objects.all() [:10000] #show only 5000 record in the table
    #all_count = Alst.objects.count()
    #alst_count = Alst.objects.filter( Q(type__exact= "ALST")).count()
    #mndx_count = Alst.objects.filter(Q(type__exact="MNDX")).count()


# Create your views here.

def home (request):
    return render(request, 'sssa_home.html')

def alst_create_record(request):
    alst_record_form = AlstForm(request.POST or None)
    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('ssa_home')

    return render(request, 'forms/alst_record_form.html', {'alst_record_form': alst_record_form})


def alst_details_record(request, id):
    alst_record = Alst.objects.get(id=id)
    return render(request, 'forms/alst_details.html', {'alst_record': alst_record})



def alst_update_record(request, id):
    alst_record = Alst.objects.get(id=id)
    alst_record_form = AlstForm(request.POST or None, instance=alst_record)

    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('ssa_home')

    return render(request, 'forms/alst_record_form.html', {'alst_record': alst_record, 'alst_record_form': alst_record_form})

def alst_delete_record(request, id):
    alst_record = Alst.objects.get(id=id)

    if request.method == 'POST':
        alst_record.delete()
        return redirect('sssa_home')

    return render(request, 'forms/record_delete_confirmation.html', {'alst_record': alst_record})