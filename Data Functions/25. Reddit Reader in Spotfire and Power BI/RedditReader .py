import praw
import pandas as pd 
from tabulate import tabulate
# Get your credentials from https://www.reddit.com/prefs/apps

reddit = praw.Reddit(
    client_id="getUrOwnCientID",
    client_secret="getUrOwnSecret",
    user_agent="my user agent",
)

posts = []

new = reddit.subreddit('python').new(limit=10)

for post in new:
    posts.append([post.title, post.score, post.num_comments, post.selftext, post.created, post.pinned, post.total_awards_received])
#create a dataframe
df = pd.DataFrame(posts,columns=['title', 'score', 'comments', 'post', 'created', 'pinned', 'total awards'])

print(tabulate(df[['title','score']],headers='keys',tablefmt="pipe"))