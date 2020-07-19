from TikTokApi import TikTokApi
import random
import requests
import os

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
def gencode():
    ucode =''
    for i in range(20):
        ucode += random.choice(chars)
    return ucode

api = TikTokApi()
def getvideo(url):
    if url[8] == 'v' and url[9] == 'm':
        session = requests.Session()  # so connections are recycled
        url = session.head(url, allow_redirects=True).url
        url = url.split('/v/')
        url = url[1].split('.html')
    else:
        url = url.split('/video/')
        url = url[1].split('?')
    id = url[0]
    video_info = api.getTikTokById(id)
    video_url = video_info["itemInfo"]["itemStruct"]["video"]["downloadAddr"]
    headers = {"User-Agent": "okhttp"}
    video_data = requests.get(video_url)
    video_data = video_data.content
    with open('data.txt', 'wb') as out:
        out.write(video_data)

    name = gencode() + '.mp4'

    f = open('data.txt',encoding="utf8", errors='replace')
    text = f.read()
    vid = text.find("vid:")
    pos = text[vid+4:vid+36]
    f.close()
    os.remove('data.txt')

    video_url_no_wm = "https://api2-16-h2.musical.ly/aweme/v1/play/?video_id={" \
                    "}&vr_type=0&is_play_url=1&source=PackSourceEnum_PUBLISH&media_type=4" \
        .format(pos)
    video_data_no_wm = requests.get(video_url_no_wm, params=None, headers=headers)
    
    
    with open("download_videos/" + name, 'wb') as out:
        out.write(video_data_no_wm.content)

    return name
