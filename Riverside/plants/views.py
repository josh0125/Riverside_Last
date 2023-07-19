from django.shortcuts import render, redirect
from .models import Plant, Category
from django.core.paginator import Paginator
from django.db.models import Q
from functools import reduce



# Create your views here.


# INDEX PAGE
def indexPage(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/index.html', context)

# CONTACT PAGE
def contactPage(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/contact.html', context)

# ERROR PAGE
def error_404(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/error.html', context)


# PLANT PAGE
def plantPage(request):
    this_year = True

    data = Plant.objects.get_queryset()

    if this_year:
        data = data.filter(this_year=True)

    data = data.order_by('id')
    #data = Plant.objects.get_queryset().order_by('id')
    #data = Plant.objects.all()

    items_per_page = 9
    paginator = Paginator(data, items_per_page)

    page_number = request.GET.get('page')

    if not page_number:
        page_number = 1

    page = paginator.get_page(page_number)
    
    categories = Category.objects.all()

    context = {
        "plants" : data,
        "categories" : categories,
        "page": page
    }
    return render(request, 'plants/plants.html', context)

def onePlantDisplayPage(request, iID):
    data = Plant.objects.get(id=iID)
    categories = Category.objects.all()
    
    user = data.uses_characteristics
    lines = user.split(";")
    for line in lines:
        print(line.strip())

    context = {
        "plant" : data,
        "categories" : categories,
        "lines" : lines
    }
    return render(request, 'plants/display.html', context)


# CATEGORY PAGES
def categoryPage(request):
    data = Category.objects.all()
    categories = Category.objects.all()

    context = {
        "categories" : data
    }
    return render(request, 'plants/category.html', context)

# Filters all Plants with that specific category
def categoryDisplayPage(request, sName):
    this_year = True
    category = Category.objects.get(name=sName)
    categories = Category.objects.all()

    data = Plant.objects.get_queryset().filter(category = category)

    if this_year:
        data = data.filter(this_year=True)

    data = data.order_by('id')
    #data = Plant.objects.filter(category = category)

    items_per_page = 9
    paginator = Paginator(data, items_per_page)

    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1

    page = paginator.get_page(page_number)

    context = {
        "plants" : data,
        "category" : category,
        "categories" : categories,
        "page": page
    }
    return render(request, 'plants/plants.html', context)


# Search Pages
def searchPage(request):
    search = (request.GET['search'])
    if search == '':
        return redirect('index')

    page_number = (request.GET.get('page'))
    #data = Plant.objects.get_queryset().filter(variety__icontains=search).order_by('variety')
    # data = Plant.objects.filter(variety__icontains=search)
    search_terms = search.split()
    for term in search_terms:
        print('x')
    # data = Plant.objects.filter(
    #     reduce(lambda x, y: x | y, [Q(variety__icontains=search) |
    #     Q(pronunciation__icontains=search) |
    #     Q(botanical_name__icontains=search) |
    #     Q(aliases__icontains=search) |
    #     Q(description__icontains=search) |
    #     Q(zone__icontains=search) |
    #     Q(min_temp__icontains=search) |
    #     Q(tips__icontains=search) |
    #     Q(difficulty__icontains=search) |
    #     Q(height__icontains=search) |
    #     Q(spread__icontains=search) |
    #     Q(growth_rate__icontains=search) |
    #     Q(companion_plant__icontains=search) |
    #     Q(blooming_fruiting__icontains=search) |
    #     Q(summer_foliage__icontains=search) |
    #     Q(fall_foliage__icontains=search) |
    #     Q(flower_color__icontains=search) |
    #     Q(uses_characteristics__icontains=search) |
    #     Q(price__icontains=search) |
    #     Q(category__name__icontains=search) |
    #     Q(subcategory__name__icontains=search) |
    #     Q(sun_exposure__description__icontains=search) |
    #     Q(soil_type__description__icontains=search) |
    #     Q(soil_moisture__description__icontains=search) |
    #     Q(habit__description__icontains=search) for term in search_terms])
    # )

    query_filters = [Q(variety__icontains=search) | Q(pronunciation__icontains=search) |  Q(botanical_name__icontains=search) | Q(aliases__icontains=search) | Q(description__icontains=search) | Q(zone__icontains=search) | Q(min_temp__icontains=search) | Q(tips__icontains=search) | Q(difficulty__icontains=search) | Q(height__icontains=search) | Q(spread__icontains=search) | Q(growth_rate__icontains=search) | Q(companion_plant__icontains=search) | Q(blooming_fruiting__icontains=search) | Q(summer_foliage__icontains=search) | Q(fall_foliage__icontains=search) | Q(flower_color__icontains=search) | Q(uses_characteristics__icontains=search) | Q(price__icontains=search) | Q(category__name__icontains=search) | Q(subcategory__name__icontains=search) | Q(sun_exposure__description__icontains=search) | Q(soil_type__description__icontains=search) | Q(soil_moisture__description__icontains=search) | Q(habit__description__icontains=search) for search in search_terms]
    combined_filter = Q(*query_filters)

    data = Plant.objects.filter(combined_filter)


    items_per_page = 9
    paginator = Paginator(data, items_per_page)

   
    if not page_number:
        page_number = 1

    page = paginator.get_page(page_number)

    categories = Category.objects.all()
    context = {
        "plants" : data,
        "categories" : categories,
        "search": search,
        "page": page
    }

    return render(request, 'plants/plants.html', context)


# TAG PAGE
def tagPage(request):
    data = Plant.objects.all()
    categories = Category.objects.all()
    page_number = (request.GET.get('page'))


    if not page_number:
        page_number = 1

    items_per_page = 8
    paginator = Paginator(data, items_per_page)

    page = paginator.get_page(page_number)

    context = {
        "plant" : data,
        "categories" : categories,
        "page": page
    }
    return render(request, 'plants/tags.html', context)


# SEARCH TAGS
def searchTagPage(request):
    search = (request.GET['searchtags'])
    if search == '':
        return redirect('index')

    page_number = (request.GET.get('page'))

    search_terms = search.split()

    query_filters = [Q(variety__icontains=search) | Q(pronunciation__icontains=search) |  Q(botanical_name__icontains=search) | Q(aliases__icontains=search) | Q(description__icontains=search) | Q(zone__icontains=search) | Q(min_temp__icontains=search) | Q(tips__icontains=search) | Q(difficulty__icontains=search) | Q(height__icontains=search) | Q(spread__icontains=search) | Q(growth_rate__icontains=search) | Q(companion_plant__icontains=search) | Q(blooming_fruiting__icontains=search) | Q(summer_foliage__icontains=search) | Q(fall_foliage__icontains=search) | Q(flower_color__icontains=search) | Q(uses_characteristics__icontains=search) | Q(price__icontains=search) | Q(category__name__icontains=search) | Q(subcategory__name__icontains=search) | Q(sun_exposure__description__icontains=search) | Q(soil_type__description__icontains=search) | Q(soil_moisture__description__icontains=search) | Q(habit__description__icontains=search) for search in search_terms]
    combined_filter = Q(*query_filters)

    data = Plant.objects.filter(combined_filter)


    items_per_page = 9
    paginator = Paginator(data, items_per_page)

   
    if not page_number:
        page_number = 1

    page = paginator.get_page(page_number)

    categories = Category.objects.all()
    context = {
        "plants" : data,
        "categories" : categories,
        "searchtag": search,
        "page": page
    }

    return render(request, 'plants/tags.html', context)

