from django.shortcuts import render, redirect
from .models import Alst, AlstTable
from .forms import *
from .filters import AlstFilter
from django.db.models import Q
from django.db.models import F
from .models import *
from django.shortcuts import render, get_object_or_404




# Create your views here.
def index (request):
    alst_filter = AlstFilter(request.GET, queryset=Alst.objects.all())
    # Get the filtered queryset
    alst_records = alst_filter.qs

    # Count how many records are in the filtered queryset
    record_count = alst_records.count()

    context = {
        'form': alst_filter.form,
        'alst_records': alst_filter.qs,
        'record_count': record_count,  # Count of the filtered records

    }
    return render(request, 'index.html', context)


def home (request):
    return render(request, 'sssa_home.html')

def collections (request):
    return render(request, 'collections.html')

def search_view(request):
    query = request.GET.get('q', '')
    type_filter = request.GET.get('type_filter', '')
    title_filter = request.GET.get('title_filter', '')
    informant_filter = request.GET.get('informant_filter', '')
    results = Alst.objects.all()

    if query:
        results = results.filter(

            Q(catalogue_number__icontains=query) |
            Q(type_of_material__icontains=query) |
            Q(parent__icontains=query) |
            Q(summary__icontains=query) |
            Q(informant_artist__icontains=query) |
            Q(title__icontains=query)
        )

    if type_filter:
        results = results.filter(type__iexact=type_filter)
    if title_filter:
        results = results.filter(title__icontains=title_filter)
    if informant_filter:
        results = results.filter(informant_artist__icontains=informant_filter)

    return render(request, 'search_view.html', {
        'results': results,
        'query': query,
        'type_filter': type_filter,
        'title_filter': title_filter,
        'informant_filter': informant_filter
    })

def alst_create_record(request):
    alst_record_form = AlstForm(request.POST or None)
    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('search_view')

    return render(request, 'forms/alst_record_form.html', {'alst_record_form': alst_record_form})


def alst_details_record(request, id):
    urls = Alst.extract_word_matereial
    alst_all_records=Alst.objects.all()
    alst_record = Alst.objects.get(id=id)
    related_records = Alst.objects.filter(parent = alst_record.catalogue_number).exclude(id=id)
    return render(request, 'forms/alst_details.html', {
        'alst_record': alst_record,
        'alst_all_records': alst_all_records,
        'related_records': related_records,
        'urls': urls,
    })



def alst_update_record(request, id):
    alst_record = Alst.objects.get(id=id)
    alst_record_form = AlstForm(request.POST or None, instance=alst_record)

    if alst_record_form.is_valid():
        alst_record_form.save()
        return redirect('search_view')

    return render(request, 'forms/alst_record_form.html', {'alst_record': alst_record, 'alst_record_form': alst_record_form})

def alst_delete_record(request, id):
    alst_record = Alst.objects.get(id=id)

    if request.method == 'POST':
        alst_record.delete()
        return redirect('alst_table')

    return render(request, 'forms/record_delete_confirmation.html', {'alst_record': alst_record})


def filtered_items(request, word):
    # This filters items where the 'material' field contains the word (case-insensitive)
    items = Alst.objects.filter(type_of_material__icontains=word)
    count_items = Alst.objects.filter(type_of_material__icontains=word).count
    return render(request, 'filtered_items.html', {
        'items': items,
        'word': word,
        'count_items': count_items,
    })