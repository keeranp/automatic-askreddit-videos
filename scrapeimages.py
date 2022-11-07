import os


def take_screenshots(content, page):
    print("Taking screenshots")

    title_path = os.path.join("assets", "images", "title.png")

    post_url = content["url"]
    page.goto(post_url, timeout=0)
    print(post_url)
    page.locator('[data-test-id="post-content"]').screenshot(path=title_path)

    for comment in content["comments"]:
        path = os.path.join("assets", "images", str(comment["id"]) + ".png")
        page.goto("https://www.reddit.com"+comment["url"], timeout=0)
        page.locator(f".Comment.t1_{comment['id']}").screenshot(path=path)
