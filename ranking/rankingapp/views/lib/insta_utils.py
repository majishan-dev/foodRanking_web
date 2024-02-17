from django.shortcuts import render
from django.views.generic import ListView, TemplateView
import requests
import json
import os

def post(post_hashtag):
    settings = load_settings("auth.json")
    hash_tag_name = post_hashtag
    insta_business_id = settings["insta_business_id"]
    access_token = settings["access_token"]

    hash_tag_id = get_ig_hash_id(insta_business_id, hash_tag_name, access_token)
    if hash_tag_id:
        data = search_top_hash_tag_posts(insta_business_id, hash_tag_id, access_token)
        return data



# 読み込み関数
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

