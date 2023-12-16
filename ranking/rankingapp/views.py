from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import RankingModel

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = RankingModel

class RankingHome(TemplateView):
    template_name = 'home.html'
    