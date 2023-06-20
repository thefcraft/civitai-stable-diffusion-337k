import json, csv
# (!wget https://huggingface.co/datasets/thefcraft/civitai-stable-diffusion-337k/resolve/main/othertype/civitai.csv) download civitai.json from huggingface🤗

with open('civitai.json', 'rb') as f:
    data = json.load(f)
    
keys = tuple(data['items'][0].keys())
meta_keys = ('prompt', 'negativePrompt', 'steps', 'sampler', 'seed', 'Size', 'Model')

def get_meta(i, j):
    if i.get('meta'):
        return i.get('meta').get(j)
    else: return None

def get_data(i, j):
    if j in meta_keys:
        return get_meta(i, j)
    else: return i.get(j)
 
 
get_keys = 'id, prompt, negativePrompt, steps, sampler, seed, Model, url, hash, nsfw, width, height, Size, createdAt, postId, stats, meta, username'.replace(',','').split(' ')

with open('civitai.csv', 'w', newline='', encoding='utf') as file:
    writer = csv.writer(file)
     
    writer.writerow(get_keys)

    for i in data['items']:
        key_datas = []
        for get_key in get_keys:
            key_data = get_data(i, get_key)
            key_datas.append(key_data)
        writer.writerow(key_datas)
        
import pandas as pd
df = pd.read_csv('civitai.csv', dtype={"seed": float})
df.to_parquet('civitai.parquet')

from huggingface_hub import login
login()

from huggingface_hub import HfApi
api = HfApi()
api.upload_file(
    path_or_fileobj="civitai.parquet",
    path_in_repo="data/train-00000-of-00001-ace5b28cebba25a7.parquet",
    repo_id="thefcraft/civitai-stable-diffusion-337k",
    repo_type="dataset",
)
api.upload_file(
    path_or_fileobj="civitai.csv",
    path_in_repo="othertype/civitai.csv",
    repo_id="thefcraft/civitai-stable-diffusion-337k",
    repo_type="dataset",
)
