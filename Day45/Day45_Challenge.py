import pandas as pd
import requests
from bs4 import BeautifulSoup

yc_response = requests.get('https://news.ycombinator.com/news')
yc_webpage = yc_response.text

soup = BeautifulSoup(yc_webpage, features='html.parser')
news_title_span_tags = soup.find_all(name='span', class_='titleline')
news_title = []
news_link = []
for tag in news_title_span_tags:
    news_titles_anchor_tags = tag.find(name='a')
    news_title.append(news_titles_anchor_tags.text)
    news_link.append(news_titles_anchor_tags.get(key='href'))

news_upvotes = [int(span_tag.text.split(' ')[0]) for span_tag in soup.find_all(name='span', class_="score")]

news_details = pd.DataFrame(data={
    'Title': news_title,
    'Link': news_link,
    'Upvote': news_upvotes
})
news_details.sort_values(by='Upvote', ascending=False, inplace=True)

top_article_of_the_day = news_details.iloc[0]
print('The top article for today is' + top_article_of_the_day.Title + '\nLink to article: '
      + top_article_of_the_day.Link + f'\nIt has {top_article_of_the_day.Upvote} votes.')
