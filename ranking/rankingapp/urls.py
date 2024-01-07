from django.urls import path
from .views import TodoList, RankingHome

urlpatterns = [
    path('list/', TodoList, name='list'),
    path('home/', RankingHome.as_view(), name='home'),
]
