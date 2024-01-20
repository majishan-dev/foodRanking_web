from django.urls import path
from .views import TodoList, RankingHome, RankingList

urlpatterns = [
    path('list/', TodoList, name='list'),
    path('list_test/', RankingList.as_view(), name='list_test'),
    path('home/', RankingHome.as_view(), name='home'),
]
