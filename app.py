import os
import sys
import time
import urllib
import urllib.request
from contextlib import closing
from os import system
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


def convert_bytes(num):
    step_unit = 1000.0

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * (int(duration) + 1)))
    percent = min(int(count*block_size*100/total_size),100)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed " %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def save(url, filename):
    urllib.request.urlretrieve(url, filename, reporthook)

audio_dest = "audio"
video_dest = "video"

if not os.path.exists(audio_dest):
    os.makedirs(audio_dest)
if not os.path.exists(video_dest):
    os.makedirs(video_dest)

splash = """
  ___                _               _    __   __ ___   ___    ___  _                       
 | __|__ _  __  ___ | |__  ___  ___ | |__ \ \ / // _ \ |   \  | _ \(_) _ __  _ __  ___  _ _ 
 | _|/ _` |/ _|/ -_)| '_ \/ _ \/ _ \| / /  \ V /| (_) || |) | |   /| || '_ \| '_ \/ -_)| '_|
 |_| \__,_|\__|\___||_.__/\___/\___/|_\_\   \_/  \___/ |___/  |_|_\|_|| .__/| .__/\___||_|  
                                                                      |_|   |_|             
"""
print(splash)

print('-------------------------\n')

date = input('Name your file (no spaces or special characters): ')
system("title Scraping: "+date)

url_to_scrape = input('Facebook VOD URL: ')

print('\n-------------------------')

print('\nFinding download links...')

page = requests.get(f'https://distillvideo.com/?url={url_to_scrape}')
soup = BeautifulSoup(page.text, 'html.parser')

links = []

for table in soup.findAll('tbody'):
    for tr in table.findAll('tr'):
        for a in tr.findAll('a'):
            links = [a['href']]

            for link in links:
                with closing(urlopen(link)) as response:
                    size = response.headers['Content-Length']
                    url = link

                    if not os.path.exists(date):
                        os.makedirs(date)

                    with open(os.path.join(date, size), 'w') as out:
                        out.write(url)

                        print('Link found!')

time.sleep(1)
print('\nFinding highest quality files to download...')

for root, dirs, files in os.walk(date):
    list_of_files = []
    for name in files:
        list_of_files.append(int(name))

    sortedlist = []
    sortedlist = sorted(list_of_files)

    video = max(sortedlist)
    audio = min(sortedlist)

    video_size = convert_bytes(video)
    audio_size = convert_bytes(audio)

    print(f'\nVideo Size: {video_size}')
    print(f'Audio Size: {audio_size}')

    video = str(video)
    audio = str(audio)

    with open(os.path.join(date, video), 'r') as video_url_path:
        video_url = video_url_path.read()

    with open(os.path.join(date, audio), 'r') as audio_url_path:
        audio_url = audio_url_path.read()

    print('\nDownloading audio: ')
    save(audio_url, os.path.join(audio_dest, date + ".mp4"))

    print('\nDownloading video: ')
    save(video_url, os.path.join(video_dest, date + ".mp4"))

    print('\n\nDownload complete!')
    print('\nUse the included merge.bat file to merge the audio and video streams.')
    print('\n')
    
    system("title Scraping: Done!")
