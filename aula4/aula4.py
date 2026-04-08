from bs4 import BeautifulSoup
import requests

url = ("https://userinyerface.com/")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

print(html)
print(soup)

important_paragraphs = soup('p', {'class': 'important'})

spans_inside_divs = [span
                     for div in soup('div')
                     for span in div('span')]

print(important_paragraphs)
print(spans_inside_divs)