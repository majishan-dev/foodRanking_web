from instagram_api_get_data import load_settings, get_ig_hash_id, search_top_hash_tag_posts

def main():
    settings = load_settings("auth.json")
    hash_tag_name = "ラーメン"
    insta_business_id = settings["insta_business_id"]
    access_token = settings["access_token"]
    
    hash_tag_id = get_ig_hash_id(insta_business_id, hash_tag_name, access_token)
    if hash_tag_id:
        search_top_hash_tag_posts(insta_business_id, hash_tag_id, access_token)


if __name__ == "__main__":
    main()