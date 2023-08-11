import instaloader
import shutil
import pathlib
from datetime import date
import os

def download_instagram_reel(url):
    loader = instaloader.Instaloader()

    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
    except Exception as e:
        print("Failed to fetch the Instagram reel:", e)
        return

    if post.is_video:
        try:
            loader.download_post(post, target=f"Video")
            print("Reel downloaded successfully.")
        except Exception as e:
            print("Failed to download the Instagram reel:", e)
    else:
        print("The provided URL does not point to an Instagram reel.")

reel_url = input("Enter the Instagram reel URL: ")
# save_path = input("Enter the path to save the video: ")

download_instagram_reel(reel_url)
