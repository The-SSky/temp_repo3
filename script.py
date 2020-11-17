import requests
from bs4 import BeautifulSoup

def save_domino_pizzas():
    with open(r'domino.htm', 'wb') as pizza_file:
        pizza_file.write(response.content)

def parse_a_block():
    pass

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) ' 
        + 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36'}

url = r'https://samara.dominospizza.ru/category/picca'

response = requests.get(url, headers=headers)

with open(r'domino.htm', 'r', encoding='utf-8') as df:
    soup = BeautifulSoup(df, 'lxml')



#soup = soup.findAll('div', {'class': 'sc-1fleilf-4 bxQMRG'})

soup = soup.find('body')
soup = soup.findAll('div', recursive=False)[0]
soup = soup.findAll('div', recursive=False)[0]
soup = soup.findAll('div', recursive=False)[2]
soup = soup.findAll('div', recursive=False)[1]
soup = soup.findAll('div', recursive=False)[0]
soup = soup.findAll('div', recursive=False)[0]
soup = soup.findAll('div', recursive=False)


for i, d in enumerate(soup):
    print(f"------ {i:03d}")
    print(d.text)


#/html/body/div[1]/div/div[3]/div[2]/div/div

##
#soup = soup.findAll('div', {'class': 'ts-message acc-message-list-focusable has-replies no-padding-vertical'})
##