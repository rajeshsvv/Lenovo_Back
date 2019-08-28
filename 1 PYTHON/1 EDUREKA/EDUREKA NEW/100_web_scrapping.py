'''
import requests

# r=requests.get("http://www.thomascook.in/tcportal/india-holidays/karnataka-holiday-packages?hldplace=Kerala")
r=requests.get("https://www.edureka.co/")
c=r.content
print(type(c))
c=str(c)

with open("data.txt","w") as f:
    content=f.write(c)
    print(content)

print(type(c))

'''

import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.thomascook.in/tcportal/india-holidays/karnataka-holiday-packages?hldplace=Kerala")

c=r.content
soup=BeautifulSoup(c,"html.parser")
print(type(soup))
print(soup.prettify())
soup=str(soup)

# with open("data.txt","w") as f:
#     content=f.write(soup)
#     print(soup)

for web_link in soup.find_all('a'):
    print(web_link.get("href"))
# print(soup.prettify())

