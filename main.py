from dotenv import load_dotenv
import praw
import os

from retrievedata import retrieve_data
from playwright.sync_api import sync_playwright

from utils import create_folders
from texttospeech import text_to_speech
from scrapeimages import take_screenshots
from tqdm import tqdm

create_folders()

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    user_agent=os.environ["USER_AGENT"],
)

contents = retrieve_data(reddit, limit=1)

with sync_playwright() as p:
    print("Loading browser")

    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.reddit.com/", timeout=0)
    page.on("dialog", lambda dialog: dialog.accept())

    if page.get_by_text("Rejeter les cookies non essentiels").count() != 0:
        page.get_by_text("Rejeter les cookies non essentiels").click()

    for content in tqdm(contents):
        text_to_speech(content)
        take_screenshots(content, page)

    browser.close()
