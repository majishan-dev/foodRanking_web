from django.shortcuts import render
from django.views.generic import ListView, TemplateView
import requests
import json
import os

def get_hotpepperlist(word):
    url = f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    API_key = "dbe4e5730a0f5678"
    body = {"key": API_key, "keyword": word, "format": "json", "count": 20}
    respons = requests.get(url, body)
    return respons

