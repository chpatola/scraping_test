from urllib.request import urlopen
from bs4 import BeautifulSoup

#Scraping info from a my own app

index_url = 'https://aidadanceschool.herokuapp.com/'
page = urlopen(index_url)

soup = BeautifulSoup(page, 'html.parser')
print(soup)

#We want to find the content in the h2 heading
testTitle = soup.find('h2')
text_testTitle = testTitle.text.strip()
print("H2 headings:", text_testTitle)

#We want to get the contents of everything with class note but need selenium bcs it comes from react
#Scraping info from yths contact page
jobisida_url ='https://www.yths.fi/yhteystiedot'
jobPage = urlopen(jobisida_url)
soup1 = BeautifulSoup(jobPage, 'html.parser')
print(soup1)

#We want to find all links on the page
content = soup1.find_all('a',href=True)
print(content)

for link in content:
    print(link.get('href'))
