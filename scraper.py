import json
import os
import re
import string

import requests
from bs4 import BeautifulSoup

def remove_punct(txt):
    new_txt = txt.replace(' — ', ' ')
    new_txt = new_txt.translate(name.maketrans("", "", string.punctuation))
    new_txt = new_txt.translate(name.maketrans(" ", "_", "‘—"))
    return new_txt

def load_api(url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    return r

articles = []

# url = input("Input the URL:\n")
url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
dom = "https://www.nature.com"
art_list = []
page_num = 4
art_type = "Research Highlight"

page_num = int(input())
art_type = input()

# "News & Views", "News Feature" and "Research Highlight"

for n in range(page_num):
    dir_name = f"Page_{n + 1}"
    os.mkdir(dir_name)
    # print(dir_name)
    url_p = f"{url}&page={n + 1}"
    r = load_api(url_p)
# if r.status_code != 200:
#     print(f"\nThe URL returned {r.status_code}")
# else:
    soup = BeautifulSoup(r.content, 'html.parser')
    arts = soup.find_all('article')
    for art in arts:
        sp = art.find('span', {'class':'c-meta__type'})
        # print(sp.text)
        if sp.text == art_type:
            a = art.find('a', {'data-track-action':'view article'})
            href = a['href']
            name = a.text
            # print(name)
            fn = remove_punct(name) + ".txt"
            r = load_api(dom + href)
            if r.status_code == 200:
                soup_a = BeautifulSoup(r.content, 'html.parser')
                body = soup_a.find('div', class_=re.compile(".*article.*body.*"))
                if not body:
                    body = soup_a.find('article')
                if body and body.text:
                    text = body.text.strip()
                    fn = os.path.join(dir_name, fn)
                    with open(fn, 'wb') as file:
                        file.write(bytes(text, encoding='utf-8'))
                    art_list.append(fn)
print(f"Saved articles ({len(art_list)}):  {art_list}")
