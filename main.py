from dotenv import load_dotenv
import praw
import os
import asyncio
from retrievedata import retrieve_data
from playwright.async_api import async_playwright

from utils import create_folders
from texttospeech import text_to_speech
from scrapeimages import take_screenshots
from makevideo import make_video
from tqdm import tqdm

MAX_LENGTH = 50


async def main():
    create_folders()

    load_dotenv()

    reddit = praw.Reddit(
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        user_agent=os.environ["USER_AGENT"],
    )

    contents = retrieve_data(reddit, limit=1)

    async with async_playwright() as p:
        print("Loading browser")

        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.reddit.com/", timeout=0)
        page.on("dialog", lambda dialog: dialog.accept())

        if await page.get_by_text("Rejeter les cookies non essentiels").count() != 0:
            await page.get_by_text("Rejeter les cookies non essentiels").click()

        for content in tqdm(contents):
            await text_to_speech(content)
            await take_screenshots(content, page)
            make_video(content)

        browser.close()


asyncio.run(main())
