from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import RankingModel, InstaModel
import requests
import json
import os

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


def InstaList(request):
    object_list = InstaModel.objects.all()
    print(object_list)
    return render(request, "InstaList.html", {"object_list": object_list})


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


class RankingHome(TemplateView):
    template_name = "home.html"


# ここから下はインスタグラムのAPIからデータを取ってくる部分
def load_settings(file_name):
    """設定ファイルを読み込んで辞書として返す。"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r") as file:
        return json.load(file)


def get_ig_hash_id(business_id, hash_tag_name, access_token):
    """InstagramのハッシュタグIDを取得する。"""
    url = f"https://graph.facebook.com/v17.0/ig_hashtag_search?user_id={business_id}&q={hash_tag_name}&access_token={access_token}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["data"][0]["id"]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as error:
        print("Instagram APIのリクエスト中にエラーが発生しました:", error)
    return None


def search_top_hash_tag_posts(business_id, hash_tag_id, access_token):
    """指定したハッシュタグIDのトップ投稿を検索する。"""
    url = f"https://graph.facebook.com/{hash_tag_id}/recent_media?user_id={business_id}&fields=caption,comments_count,id,like_count,media_type,media_url,permalink,timestamp,children%7Bmedia_url%7D&access_token={access_token}&limit=10"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        instagram_media = data.get("data")
        # print(instagram_media)  # データ出力
        return instagram_media
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as error:
        print("Instagram APIのリクエスト中にエラーが発生しました:", error)
    return None


def post(post_hashtag):
    settings = load_settings("auth.json")
    hash_tag_name = post_hashtag
    insta_business_id = settings["insta_business_id"]
    access_token = settings["access_token"]

    hash_tag_id = get_ig_hash_id(insta_business_id, hash_tag_name, access_token)
    if hash_tag_id:
        data = search_top_hash_tag_posts(insta_business_id, hash_tag_id, access_token)
        return data
