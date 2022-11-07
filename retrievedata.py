from praw import Reddit
from tqdm import tqdm


def retrieve_data(reddit_client: Reddit, limit=10):
    print("Retrieving data")

    contents = []

    for submission in tqdm(reddit_client.subreddit("TooAfraidToAsk+AskReddit").hot(limit=limit)):
        content = {}
        content["url"] = submission.url
        content["title"] = submission.title
        content["comments"] = []

        for i in range(min(10, len(submission.comments))):
            content["comments"].append(
                {
                    "url": submission.comments[i].permalink,
                    "id": submission.comments[i].id,
                    "body": submission.comments[i].body,
                }
            )
        
        contents.append(content)

    return contents
