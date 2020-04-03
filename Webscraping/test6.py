# Save webscraping to CSV
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
        vid_source = article.find('iframe', class_='youtube-player')['src'] #access a tags attribute like a python dictionary
        #print(vid_source)

        # Looking for video ID. So split the vid_source string using forward slashes
        vid_id = vid_source.split('/')[4] # get the 5th element cause that's where the video id is located
        vid_id = vid_id.split('?') # now split using '?' cause the actual vid id is the string before the '?' mark 
        vid_id = vid_id[0] #this is the actual video ID

        # now to create our own youtube link
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    
    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()