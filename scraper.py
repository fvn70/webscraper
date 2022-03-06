import os
import re
import string

import requests
from bs4 import BeautifulSoup

def load_api(url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    return r

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
dom = "https://www.nature.com"
art_list = []
art_type = "News"
page_num = 4
art_type = "Research Highlight"

page_num = int(input())
art_type = input()

for n in range(page_num):
    dir_name = f"Page_{n + 1}"
    os.mkdir(dir_name)
    url_p = f"{url}&page={n + 1}"
    r = load_api(url_p)

    soup = BeautifulSoup(r.content, 'html.parser')
    arts = soup.find_all('article')
    for art in arts:
        sp = art.find('span', {'class':'c-meta__type'})
        if sp.text == art_type:
            a = art.find('a', {'data-track-action':'view article'})
            href = a['href']
            name = a.text
            fn = f"{name.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')}.txt"
            r = load_api(dom + href)
            if r.status_code == 200:
                soup_a = BeautifulSoup(r.content, 'html.parser')
                body = soup_a.find('div', class_=re.compile(".*article.*body.*"))
                fn = os.path.join(dir_name, fn)
                with open(fn, 'wb') as file:
                    file.write(bytes(body.text.strip(), encoding='utf-8'))
                art_list.append(fn)
print(f"Saved articles ({len(art_list)}):  {art_list}")
