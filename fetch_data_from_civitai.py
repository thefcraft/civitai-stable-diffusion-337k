import requests
import json

url = 'https://civitai.com/api/v1/images'

while True:
    data = requests.get(url)
    data = json.loads(data.content)
    url = data['metadata'].get('nextPage')
    if url == None: break

    items = data['items']
    # now do whatever you want with data

    break # remove this line
