## Description:

### Overview:

The Civitai Stable Diffusion 337k is a dataset containing 337k Civitai image URLs accompanied by detailed prompts and other meta-information. The dataset is primarily sourced using the Civitai API to obtain an exhaustive list of prompts associated with each image.

[Explore the dataset on HuggingFace🤗](https://huggingface.co/datasets/thefcraft/civitai-stable-diffusion-337k)

### Quick Usage:
```python
from datasets import load_dataset

dataset = load_dataset("thefcraft/civitai-stable-diffusion-337k")
print(dataset['train'][0])
```

### Dataset Structure:

The primary dataset is structured in JSON, huggingface format with a detailed breakdown of image attributes for each item. An individual item contains:

- Image URL, Hash, Dimensions, NSFW flag, Creation date, and Post ID.
- Statistical data like cry, laugh, like, dislike, heart counts, and comment count.
- Metadata including model details, prompts, sampler info, and other configuration details.
- User details for each image.

A sample structure is provided below:
```json
{
    'items': [
      {
       'id': 100657,
       'url': 'https://imagecache.civitai.com/...',
       ...
       'username': 'NeoClassicalRibbon'
      },
      ...
    ],
    'metadata':{'totalItems': 327145}
}
```

```python
{
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

### Project and Training:

An AI model was trained on this dataset for NSFW prompt detection. Details and code for the project can be found at [this GitHub repository](https://github.com/thefcraft/nsfw-prompt-detection-sd).
