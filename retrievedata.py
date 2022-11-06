import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    user_agent=os.environ["USER_AGENT"],
)

contents = []

for submission in reddit.subreddit("TooAfraidToAsk+AskReddit").hot(limit=10):
    content = {}
    content["url"] = submission.url
    content["title"] = submission.title
    content["comments"] = []
    print(len(submission.comments))
    for i in range(min(10, len(submission.comments))):
        content["comments"].append({
            "url": submission.comments[i].permalink,
            "id": submission.comments[i].id,
            "body": submission.comments[i].body,
        })

    # print(content)