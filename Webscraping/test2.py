from bs4 import BeautifulSoup
import requests

with open('testpage.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

match = soup.title
print(match)

match = soup.title.text
print(match)

match = soup.div    # only matchs the 1st corresponding tag
print(match)

print()
match = soup.find('div') 
print(match)
print(type(match))

print()
match = soup.find('div', class_='footer') # find allows argumets to narrow down matches
print(match)