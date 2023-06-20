# civitai-stable-diffusion-337k
### huggingface🤗 url
dataset = https://huggingface.co/datasets/thefcraft/civitai-stable-diffusion-337k

json download link = https://huggingface.co/datasets/thefcraft/civitai-stable-diffusion-337k/resolve/main/othertype/civitai.json
### How to Use
```
from datasets import load_dataset

dataset = load_dataset("thefcraft/civitai-stable-diffusion-337k")

print(dataset['train'][0])
```

### Dataset Summary

dataset:- civitai-stable-diffusion-337k this dataset contains 337k civitai images url with prompts etc. i use civitai api to get all prompts.
project:- https://github.com/thefcraft/nsfw-prompt-detection-sd  I train a model on this dataset


DATA STRUCTURE for othertype/civitai.json:-

```{
'items':[
      {'id': 100657,
       'url': 'https://imagecache.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2338276a-87f7-4a1e-f92a-776a18ee4200/width=768/2338276a-87f7-4a1e-f92a-776a18ee4200.jpeg',
       'hash': 'U5Exz_00.8D$t89Z%M0100~VD*RktQxaIU~p',
       'width': 768,
       'height': 1368,
       'nsfw': True,
       'createdAt': '2023-02-14T10:05:11.498Z',
       'postId': 60841,
       'stats': {'cryCount': 0,
                 'laughCount': 0,
                 'likeCount': 26,
                 'dislikeCount': 0,
                 'heartCount': 50,
                 'commentCount': 4},
       'meta': {'ENSD': '31337',
                'Size': '512x912',
                'seed': 3994946333,
                'Model': 'AbyssOrangeMix2_sfw',
                'steps': 20,
                'prompt': '<lora:hiqcg_body-epoch-000004:0.5>, <lora:hiqcg_face-epoch-000004:0.4>, hiqcgbody, hiqcgface, 1girl, full body, standing, \ndetailed skin texture, detailed cloth texture,  beautiful detailed face,\nmasterpiece, best quality, ultra detailed, 8k, intricate details,',
                'sampler': 'DPM++ 2M Karras',
                'cfgScale': 7,
                'Clip skip': '2',
                'resources': [{'hash': '038ba203d8',
                               'name': 'AbyssOrangeMix2_sfw',
                               'type': 'model'}],
                'Model hash': '038ba203d8',
                'Hires upscale': '1.5',
                'Hires upscaler': 'Latent',
                'negativePrompt': 'EasyNegative, extra fingers,fewer fingers, multiple girls, multiple views,',
                'Denoising strength': '0.6'},
        'username': 'NeoClassicalRibbon'},
      {..},
       ..],

'metadata':{'totalItems': 327145}
}
```
