from bs4 import BeautifulSoup
import requests

with open('testpage.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

article = soup.find('div', class_='article')
#print(article)

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

print()
print("---- List of Articles ----")
articles = soup.find_all('div', class_='article')
for article in articles:
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)
    print()