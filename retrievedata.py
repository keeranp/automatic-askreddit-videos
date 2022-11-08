from praw import Reddit


async def retrieve_data(reddit_client: Reddit, limit=10):
    print("Retrieving data")

    contents = []

    subreddits = await reddit_client.subreddit("TooAfraidToAsk+AskReddit")

    async for submission in subreddits.hot(limit=limit):
        content = {}
        content["url"] = submission.url
        content["title"] = submission.title
        content["id"] = submission.id
        content["comments"] = []
        comments = await submission.comments()
        
        for i in range(min(10, len(comments))):
            content["comments"].append(
                {
                    "url": submission.comments[i].permalink,
                    "id": submission.comments[i].id,
                    "body": submission.comments[i].body,
                }
            )
        
        contents.append(content)
    return contents
