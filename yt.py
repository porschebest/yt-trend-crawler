from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# First Step
response = requests.get('https://www.youtube.com/feed/trending')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Hot Video Author
all_text = []
length = []
title = []
author = []
for link in soup.find(role="main").find_all(attrs={"class": "yt-uix-sessionlink"}):
    all_text.append(link.get_text())
print(all_text)

# Separate all_text into three part
delta = len(all_text)/3
def extract_from_all(start,step,target):
    li = np.arange(start,len(all_text),3)
    for i in li:
        target.append(all_text[i])
    print(target)
extract_from_all(1,delta,length)
extract_from_all(2,delta,title)
extract_from_all(3,delta,author)

# Separate date and views
date = []
views = []
for link in soup.find(role="main").find_all(attrs={"class": "yt-lockup-meta-info"}):
    date.append(link.get_text().split('觀看次數：')[0])
    views.append(link.get_text().split('觀看次數：')[1])

# Hot Video time



'''
<a class="yt-uix-sessionlink spf-link "
data-sessionlink="itct=CAoQ3DAYHSITCPSayYOSsNoCFU9ZYAod9GAMZSjpHg"
href="/channel/UCvmEITnUDxirhD5VUOFt_4w">KenHo1勁好玩</a>
<a aria-describedby="description-id-12652"
class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "
data-sessionlink="itct=CAoQ3DAYHCITCJD94uWDsNoCFQJhKgodQG4JiijpHjIMdHJlbmRpbmctdHJiWgpGRXRyZW5kaW5n"
dir="ltr" href="/watch?v=Q2XNeZkoq50"
title="鋁箔紙金屬球裡面真實結構？What's INSIDE?（Aluminium Foil Ball）">
鋁箔紙金屬球裡面真實結構？What's INSIDE?（Aluminium Foil Ball）
</a>
'''

'''
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="EBORaypI8VI" onclick=";return false;" role="button" title="稍後觀看" type="button"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" data-style="tv-queue" data-video-ids="EBORaypI8VI" onclick=";return false;" title="候播清單" type="button"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a aria-describedby="description-id-188415" class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link " data-sessionlink="itct=CAoQ3DAYGyITCNChtLf1tNoCFYFmKgodaEcJ5CjpHjIMdHJlbmRpbmctdHJiWgpGRXRyZW5kaW5n" dir="ltr" href="/watch?v=EBORaypI8VI" title="我的男孩第16集預告">我的男孩第16集預告</a><span class="accessible-description" id="description-id-188415"> - 播放時間：0:29。</span></h3><div class="yt-lockup-byline ">
<a class="yt-uix-sessionlink spf-link " data-sessionlink="itct=CAoQ3DAYGyITCNChtLf1tNoCFYFmKgodaEcJ5CjpHg" href="/channel/UCvgNKuXdfNGNaEKoG4nNwRA">snsdexo love</a>
</div>
<div class="yt-lockup-meta ">
<ul class="yt-lockup-meta-info">
<li>5 天前</li>
<li>觀看次數：128,408</li>
</ul>
</div>
<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">
我的男孩  林心如 X 張軒睿<br/>下禮拜五晚間十點台視
</div></div></div></div></div></li></ul></div></div><div class="feed-item-dismissal-notices"></div></div></li>

'''
