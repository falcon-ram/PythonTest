from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

article = soup.find('article')
#print(article.prettify())

headline = article.h2.a.text
print(headline)

summary = article.find('div', class_='entry-content').p.text
print(summary)

vid_source = article.find('iframe', class_='youtube-player')
print(vid_source)

vid_source = article.find('iframe', class_='youtube-player')['src'] #access a tags attribute like a python dictionary
print(vid_source)

# Looking for video ID. So split the vid_source string using forward slashes
vid_id = vid_source.split('/')
print(vid_id)
vid_id = vid_source.split('/')[4] # get the 5th element cause that's where the video id is located
print(vid_id)
vid_id = vid_id.split('?') # now split using '?' cause the actual vid id is the string before the '?' mark 
print(vid_id)
vid_id = vid_id[0] #this is the actual video ID
print(vid_id)

# now to create our own youtube link
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)

