from django.urls import path
from .views import (
    TodoList,
    RankingHome,
    RankingList,
    RankList,
    RankListPages,
    InstaGetAPI,
    InstaList,
    InstaFormAPI,
    HotPepperList,
)

urlpatterns = [
    path("list/", TodoList, name="list"),
    path("list_test_func/", RankList, name="list_test"),
    path("list_test_func/<int:pk>/", RankListPages, name="list_test"),
    path("list_test/", RankingList.as_view(), name="home"),
    path("home/", RankingHome.as_view(), name="home"),
    path("insta_api/", InstaFormAPI, name="insta"),
    path("insta_list/", InstaList, name="instalist"),
    path("get_insta_api/", InstaGetAPI, name="getinsta"),
    path("hotpepper_list/", HotPepperList, name="hotpepperlist"),
]
