import requests

def load_api(url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    return r

url = input("Input the URL:\n")

r = load_api(url).json()
if 'content' not in r.keys():
    print(f"\nInvalid quote resource!")
else:
    print(r['content'])
