from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import RankingModel

# Create your views here.

# classbasedよりはfunctionbasedの方がよいとおもっているが認識合う？


def TodoList(request):
    range_list = range(2)
    return render(request, "list.html", {"range_list": range_list})


class RankingList(ListView):
    template_name = "rankinglist.html"
    model = RankingModel


def RankList(request):
    object_list = RankingModel.objects.all()
    print(object_list)
    return render(request, "rankinglist.html", {"object_list": object_list})


class RankingHome(TemplateView):
    template_name = "home.html"
