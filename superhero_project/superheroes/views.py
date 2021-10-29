from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero


# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes' : all_heroes
    }
    return render(request,'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero' : single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def edit(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        single_hero.name = request.POST.get('name')
        single_hero.alter_ego = request.POST.get('alter_ego')
        single_hero.primary = request.POST.get('primary')
        single_hero.secondary = request.POST.get('secondary')
        single_hero.catchphrase = request.POST.get('catchphrase')
        single_hero.save()
        return HttpResponseRedirect('superheroes:index')
    else:
        return render(request, 'superheroes/edit.html')

def delete(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        single_hero.name = request.POST.get('name')
        single_hero.alter_ego = request.POST.get('alter_ego')
        single_hero.primary = request.POST.get('primary')
        single_hero.secondary = request.POST.get('secondary')
        single_hero.catchphrase = request.POST.get('catchphrase')
        single_hero.delete(request,hero_id)
        return HttpResponseRedirect('superheroes:index')
    else:
        return render(request, 'superheroes/delete.html')