# web scrapping means parsing the content from the website and pulling out exactly information that you want
"""
examples:we want to pull down some head lines from my new site
or grab some scores from a sports website
or moniter the prices of some items in an online store something like that

we have built in URL lib module -request library is extremely popular for fetching websites

to install beautiful soap you can just use the pip install command

cmd->pip install beautifulsoap4

iam not able to install this look next into it

beautiful soap have L XML for parsing the HTML content
"""
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
