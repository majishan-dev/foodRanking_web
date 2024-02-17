from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from ..models import RankingModel, InstaModel
from .lib import post
import requests
import json
import os


def InstaList(request):
    object_list = InstaModel.objects.all()
    print(object_list)
    return render(request, "InstaList.html", {"object_list": object_list})


def InstaFormAPI(request):
    if request.method == "POST":
        hash_tag_name = "ラーメン"
        data = post(hash_tag_name)
        for i in data:
            try:
                image_url = i["media_url"]
            except:
                image_url = i["children"]["data"][0]["media_url"]
            InstaModel.objects.create(title=i["caption"], shop_image=image_url)
        return render(request, "home.html", {"data": data})
    else:
        return render(request, "InstaAPI.html")
    
    
def InstaGetAPI(request):
    return render(request, "home.html")