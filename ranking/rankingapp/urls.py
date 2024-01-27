from django.urls import path
from .views import TodoList, RankingHome, RankingList, RankList

urlpatterns = [
    path("list/", TodoList, name="list"),
    path("list_test_func/", RankList, name="list_test"),
    path("list_test/", RankingList.as_view(), name="home"),
    path("home/", RankingHome.as_view(), name="home"),
]
