"""Uses Apify to scrape tweets, based on https://twitter.wordware.ai/"""

import json
import os

import requests

API_TOKEN = os.environ.get("APIFY_API_TOKEN")
headers = {"Content-Type": "application/json"}


def read_cache(username: str, is_tweet: bool = False):
    cache_folder = os.path.join("./caches", username)
    if os.path.exists(cache_folder):
        filename = "tweets.json" if is_tweet else "profile.json"
        with open(os.path.join(cache_folder, filename), "r", encoding="utf-8") as file:
            return json.load(file)

    return None


def scrape_profile(username: str):
    if res := read_cache(username):
        return res
    data = {
        "startUrls": [f"https://twitter.com/{username}"],
        "twitterHandles": [username],
        "getFollowers": True,
        "getFollowing": True,
        "getRetweeters": False,
        "includeUnavailableUsers": False,
        "maxItems": 5,
    }
    print(data)
    url = f"https://api.apify.com/v2/acts/V38PZzpEgOfeeWvZY/run-sync-get-dataset-items?token={API_TOKEN}"
    try:
        response = requests.post(url, json=data, headers=headers)
        print("Full Response:", response.status_code, response.json())
        result = response.json()
        return result
    except requests.exceptions.RequestException as error:
        print("Full Error:", error.response)


def scrape_tweets(username: str):
    if res := read_cache(username, is_tweet=True):
        return res
    data = {
        "startUrls": [
            f"https://www.x.com/{username}",
        ],
        "maxItems": 12,
        "sort": "Latest",
        "tweetLanguage": "en",
        "customMapFunction": "(object) => { return {...object} }",
    }
    print(data)
    url = f"https://api.apify.com/v2/acts/61RPP7dywgiy0JPD0/run-sync-get-dataset-items?token={API_TOKEN}"

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Actor run successfully:", json.dumps(response.json()))
        result = response.json()
        return result
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)
