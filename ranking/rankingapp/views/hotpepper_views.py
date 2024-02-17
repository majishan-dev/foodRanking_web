from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .lib import get_hotpepperlist
from ..models import RankingModel, InstaModel
import requests
import json
import os


def HotPepperList(request):
    word = "東京駅"
    respons = get_hotpepperlist(word)
    respons_shop = respons.json()["results"]["shop"]
    shoplist = []
    for i in respons_shop:
        shoplist.append({"name": i["name"], "image": i["logo_image"]})
    # print(shoplist)
    return render(request, "HotPepperList.html", {"respons": shoplist})
