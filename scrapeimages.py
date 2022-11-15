import os
from playwright._impl._api_types import TimeoutError

async def take_screenshots(content, page):
    print("Taking screenshots")

    title_path = os.path.join("assets", "images", "title.png")

    post_url = content["url"]
    await page.goto(post_url, timeout=0)
    try:
        await page.locator('[data-test-id="post-content"]').screenshot(path=title_path)
    except TimeoutError as e:
        print(e)
        print(post_url)
        return False

    for comment in content["comments"]:
        path = os.path.join("assets", "images", str(comment["id"]) + ".png")
        await page.goto("https://www.reddit.com" + comment["url"], timeout=0)
        try:
            await page.locator(f".Comment.t1_{comment['id']}").screenshot(
                path=path,
            )
        except TimeoutError as e:
            print(e)
            print(post_url)
            return False

    return True
