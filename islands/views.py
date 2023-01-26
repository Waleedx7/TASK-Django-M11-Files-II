from django.http import HttpRequest, HttpResponse 
from django.shortcuts import render, redirect
from islands import models
from .forms import IslandForm

def get_islands(request: HttpRequest) -> HttpResponse:
    islands: list[models.Island] = list(models.Island.objects.all())

    context = {
        "islands": islands,
    }

    return render(request, "island_list.html", context)

def create_island(request):
    form = IslandForm()
    if request.method == "POST":
        form = IslandForm(request.POST, request.FILES)
        if form.is_valid():
            photos = form.cleaned_data["photos"]
            name = form.cleaned_data["name"]
            island = models.Island.objects.create(name=name)
            for photo in photos:
                models.IslandPhoto.objects.create(island=island, image=photo)

            return redirect ("island-list")

    context = {
        "form":form,
    }
    return render(request, "create_island.html", context)
