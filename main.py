#!/usr/bin/env python3

# (c) izl, 2020
# but who cares?

"""Script to download webms from 4chan's /gif/ board."""

import json
import os
import requests
from tqdm import tqdm

catalog_endpoint = 'https://a.4cdn.org/gif/catalog.json'

r = requests.get(catalog_endpoint)

pages = json.loads(r.text)

threads = []

for page in pages:
    for thread in page['threads']:
        threads.append((thread['semantic_url'], thread['no'], thread['images']))

threads.pop(0)

for i, thread in enumerate(threads):
    print('{} | I: {}\t| {}'.format(i, thread[2], thread[0]))

user_choice = input('Please make a selection (space-separated): ')

choice_list = user_choice.split(' ')

posts_collection = []

print('Fetching threads...')

for choice in choice_list:
    posts_collection.append(
        json.loads(requests.get('https://a.4cdn.org/gif/thread/{}.json'.format(
                        threads[int(choice)][1])).text))

print('Processing...')

for choice, thread in zip(choice_list, posts_collection):
    thread_title = threads[int(choice)][0]
    print(thread_title)
    webms = []
    for post in thread['posts']:
        ext_present = post.get('ext', False)
        if ext_present == '.webm':
            webms.append(post)

    os.makedirs('{}'.format(thread_title), exist_ok=True)

    for webm in tqdm(webms):
        if not os.path.exists('{}.webm'.format(webm['tim'])):
            r = requests.get('https://i.4cdn.org/gif/{}.webm'.format(webm['tim']))
            with open('{}/{}.webm'.format(thread_title, webm['filename']), 'wb') as f:
                f.write(r.content)
