from django.shortcuts import render, redirect
from .models import Alst, AlstTable
from .forms import *
from .filters import AlstFilter
from django.db.models import Q




# Create your views here.
def index (request):

    alst_filter = AlstFilter(request.GET, queryset=Alst.objects.all())
    context = {
        'form': alst_filter.form,
        'alst_records': alst_filter.qs,

    }
    return render(request, 'index.html', context)


def home (request):
    return render(request, 'sssa_home.html')


def alst_create_record(request):
    alst_record_form = AlstForm(request.POST or None)
    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('sssa_home')

    return render(request, 'forms/alst_record_form.html', {'alst_record_form': alst_record_form})


def alst_details_record(request, id):
    alst_all_records=Alst.objects.all()

    
    alst_record = Alst.objects.get(id=id)
    related_records = Alst.objects.filter(parent = alst_record.catalogue_number).exclude(id=id)
    return render(request, 'forms/alst_details.html', {
        'alst_record': alst_record,
        'alst_all_records': alst_all_records,
        'related_records': related_records,

    })



def alst_update_record(request, id):
    alst_record = Alst.objects.get(id=id)
    alst_record_form = AlstForm(request.POST or None, instance=alst_record)

    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('alst_table')

    return render(request, 'forms/alst_record_form.html', {'alst_record': alst_record, 'alst_record_form': alst_record_form})

def alst_delete_record(request, id):
    alst_record = Alst.objects.get(id=id)

    if request.method == 'POST':
        alst_record.delete()
        return redirect('alst_table')

    return render(request, 'forms/record_delete_confirmation.html', {'alst_record': alst_record})