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
def people_and_place (request):
    return render(request, 'people_and_place.html')

def subjects (request):
    return render(request, 'subjects.html')

def listen_recordings (request):
    return render(request, 'listen_recordings.html')

def search_view(request):
        query = request.GET.get('q', '')
        type_filter = request.GET.get('type_filter', '')
        collection_filter = request.GET.get('collection_filter', '')
        collection_ref_filter = request.GET.get('collection_ref_filter', '')
        informant_artist_filter = request.GET.get('informant_artist_filter', '')
        native_area_county_filter = request.GET.get('native_area_county_filter', '')
        fieldworker_filter = request.GET.get('fieldworker_filter', '')
        type_of_material_filter = request.GET.get('type_of_material_filter', '')
        title_filter = request.GET.get('title_filter', '')
        summary_filter = request.GET.get('summary_filter', '')
        catalogue_number_filter = request.GET.get('catalogue_number_filter', '')

        results = Alst.objects.all()

        if query:
            results = results.filter(
                Q(type__icontains=query) |
                Q(catalogue_number__icontains=query) |
                Q(collection__icontains=query) |
                Q(collection_ref__icontains=query) |
                Q(parent__icontains=query) |
                Q(fieldworker__icontains=query) |
                Q(date__icontains=query) |
                Q(informant_artist__icontains=query) |
                Q(native_area_county__icontains=query) |
                Q(comments__icontains=query) |
                Q(place_recorded__icontains=query) |
                Q(type_of_material__icontains=query) |
                Q(summary__icontains=query) |
                Q(disc_matrix_number__icontains=query) |
                Q(tale_reference__icontains=query) |
                Q(first_line__icontains=query) |
                Q(instrument__icontains=query) |
                Q(camera_operator__icontains=query) |
                Q(title__icontains=query) |
                Q(reference__icontains=query) |
                Q(old_number_rl__icontains=query) |
                Q(restricted__icontains=query)
            )

        if type_filter:
            results = results.filter(type__iexact=type_filter)
        if collection_filter:
            results = results.filter(collection__icontains=collection_filter)
        if collection_ref_filter:
            results = results.filter(collection_ref__icontains=collection_ref_filter)

        # 👇 Flexible matching for informant_artist
        if informant_artist_filter:
            words = informant_artist_filter.split()
            for word in words:
                results = results.filter(informant_artist__icontains=word)

        if native_area_county_filter:
            results = results.filter(native_area_county__icontains=native_area_county_filter)

        # 👇 Flexible matching for fieldworker
        if fieldworker_filter:
            words = fieldworker_filter.split()
            for word in words:
                results = results.filter(fieldworker__icontains=word)

        if type_of_material_filter:
            results = results.filter(type_of_material__icontains=type_of_material_filter)
        if title_filter:
            results = results.filter(title__icontains=title_filter)
        if summary_filter:
            results = results.filter(summary__icontains=summary_filter)
        if catalogue_number_filter:
            results = results.filter(catalogue_number__icontains=catalogue_number_filter)

        return render(request, 'search_view.html', {
            'results': results,
            'query': query,
            'type_filter': type_filter,
            'collection_filter': collection_filter,
            'collection_ref_filter': collection_ref_filter,
            'informant_artist_filter': informant_artist_filter,
            'native_area_county_filter': native_area_county_filter,
            'fieldworker_filter': fieldworker_filter,
            'type_of_material_filter': type_of_material_filter,
            'title_filter': title_filter,
            'summary_filter': summary_filter,
            'catalogue_number_filter': catalogue_number_filter
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