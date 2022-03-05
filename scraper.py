import requests
from bs4 import BeautifulSoup

def load_api(url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    return r

url = input("Input the URL:\n")
r = load_api(url)

if r.status_code != 200:
    print(f"\nThe URL returned {r.status_code}")
else:
    r = load_api(url)
    with open('source.html', 'wb') as file:
        file.write(r.content)
    print('Content saved.')


