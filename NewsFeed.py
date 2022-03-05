import feedparser
import pandas as pd
from bs4 import BeautifulSoup
rawrss = [
    customFeedURL
    ]
df=pd.DataFrame([])
for url in rawrss:
    dp = feedparser.parse(url)
    for i, e in enumerate(dp.entries):
        print(e.keys())
        feed={}
        feed['Title']= e.title if 'title' in e else 'title {i}'
        feed['Short Summary']= BeautifulSoup(e.summary if 'summary' in e else 'no summary {i}',features="lxml").get_text()
        feed['Summary']= BeautifulSoup(str(e.summary_detail.value),features="lxml").get_text()
        feed['Published']= e.published if 'published' in e else f'no published {i}'
        df=df.append(pd.DataFrame([feed]),ignore_index=True)
print(df)
#df = df.astype(str)
