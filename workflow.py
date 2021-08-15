import os

import requests
from datetime import datetime
import praw


NOTION_API_KEY= os.environ['NOTION_API_KEY']

DATABASE_KEY = 'f93f03ce6289490c9fd819000d888cf3'

def create_notionpost(title, score, subreddit, contenturl, created_date, actualurl):

    headers = {
        'Authorization': f"Bearer {NOTION_API_KEY}",
        'Content-Type': 'application/json',
        'Notion-Version': '2021-07-27',
    }
    data = { "parent": { "database_id": DATABASE_KEY }, "properties": { 
        "title": {"title": [ { "text": { "content": title } } ] },
        "score": { "number": score },
        "subreddit": { "select": { "name": subreddit } },
        # "subreddit": { "rich_text": [ { "text": { "content": subreddit } } ] },
        "contenturl": {"url": contenturl}, 
        "actualurl": {"url": actualurl}, 
        "created": {"date" : {"start": created_date}}, 
    },  }

    requests.post('https://api.notion.com/v1/pages', headers=headers, json=data)


## checks the notion block and retrieve subreddits in form of list of strings
def get_subreddits():
    headers = {
        'Notion-Version': '2021-07-27',
        'Authorization': f"Bearer {NOTION_API_KEY}",
    }
    response = requests.get('https://api.notion.com/v1/blocks/7f1b12c4517a4d2eb4157a8db89d74aa/children?page_size=10', headers=headers)
    mylist = response.json()['results'][1]['bulleted_list_item']['text'][0]['plain_text'].split()
    return mylist


def reddit_notion(subreddits):

    ## first: retrieve database and create searchable set 

    headers = {
        'Authorization': f"Bearer {NOTION_API_KEY}",
        'Notion-Version': '2021-07-27',
        'Content-Type': 'application/json',
    }
    response = requests.post('https://api.notion.com/v1/databases/f93f03ce6289490c9fd819000d888cf3/query', headers=headers)
    myneeded = response.json()['results']
    myset = set()

    for i in myneeded:
        try:
            myurl = i['properties']['actualurl']['url']
            myset.add(myurl)
        except:
            pass
    
    reddit = praw.Reddit(client_id= 'DzwOmGMsUugt5Q',
                        client_secret= 'aT3Bhzk8bFqFj7e4Jizu4GaXRAZJDw',
                        user_agent= 'hanalia_kr_tutorial_learning')
    for subreddit in subreddits:
        try:
            test_reddit = reddit.subreddit(subreddit).top("month", limit = 10)

            # test_reddit = reddit.multireddit("reactjs", "programming").top("day")
            # ml_subreddit = reddit.subreddit(mysub)
            for post in test_reddit:
                if ("https://www.reddit.com" + post.permalink) not in myset:
                    create_notionpost(post.title, post.score, subreddit, post.url, datetime.fromtimestamp(post.created).strftime("%Y-%m-%d"), ("https://www.reddit.com" + post.permalink))
        except:
            pass

targetlist = get_subreddits()
reddit_notion(targetlist)
