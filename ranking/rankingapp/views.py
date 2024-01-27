from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import RankingModel

# Create your views here.

# classbasedよりはfunctionbasedの方がよいとおもっているが認識合う？

CONTENTS_MAX = 2


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


def RankListPages(request, pk):
    object_list = RankingModel.objects.all()
    object_list_count = object_list.count()
    page_max = object_list_count // CONTENTS_MAX + 1
    object_list_page = object_list[(pk - 1) * CONTENTS_MAX : pk * CONTENTS_MAX]
    print(object_list)
    print(object_list_count)
    return render(
        request,
        "rankinglist.html",
        {
            "object_list": object_list_page,
            "page_max": page_max,
            "page": pk,
        },
    )


class RankingHome(TemplateView):
    template_name = "home.html"
