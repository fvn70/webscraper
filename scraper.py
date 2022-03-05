import requests
from bs4 import BeautifulSoup

def load_api(url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    return r

url = input("Input the URL:\n")

if 'title' not in url:
    print('\nInvalid movie page!')
else:
    dic = {}
    r = load_api(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    h_link = soup.find('h1')
    dic['title'] = h_link.text
    span_link = soup.find('span', 'GenresAndPlot__TextContainerBreakpointL-sc-cum89p-1 eqlIrG')
    dic['description'] = span_link.text
    print(dic)

