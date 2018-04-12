from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import datetime as dt

# Part 1 - Crawl Hot Video infos from YouTube
response = requests.get('https://www.youtube.com/feed/trending')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Part 2 - Get the part that we are interested - Title, Length, Author
all_text = []
length = []
title = []
author = []
for link in soup.find(role="main").find_all(attrs={"class": "yt-uix-sessionlink"}):
    all_text.append(link.get_text())

# Part 3 - Store these parts into lists
delta = len(all_text)/3
def extract_from_all(start,step,target):
    li = np.arange(start,len(all_text),3)
    for i in li:
        target.append(all_text[i])
extract_from_all(0,delta,length)
extract_from_all(1,delta,title)
extract_from_all(2,delta,author)

# delete /n/n from length
length_n = []
for i in length:
    length_n.append(i.split('\n\n')[1])

# Part 3 - Store these parts into lists - date, views
date = []
views = []
for link in soup.find(role="main").find_all(attrs={"class": "yt-lockup-meta-info"}):
    date.append(link.get_text().split('觀看次數：')[0])
    views.append(link.get_text().split('觀看次數：')[1])

# Part 4 - Store everything from lists in to DataFrame
header = ['title']
df = pd.DataFrame(title,columns=header)
def import_data(title,data):
    df[title] = data
data_header = [ 'author', 'length', 'release_date', 'views']
data = [author,length_n, date, views]
for i,v in enumerate(data):
    import_data(data_header[i],v)

# Part 5 - Get the right file name and Export
# df.to_csv('yt.csv',index=False)
file_name = str(dt.date.today()) + '-youtubeTrendsVideo.xlsx'
df.to_excel(file_name,index=False)


'''
Target text Template

</div><div class="yt-lockup-content">
<h3 class="yt-lockup-title ">
    <a aria-describedby="description-id-188415" class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link " data-sessionlink="itct=CAoQ3DAYGyITCNChtLf1tNoCFYFmKgodaEcJ5CjpHjIMdHJlbmRpbmctdHJiWgpGRXRyZW5kaW5n" dir="ltr" href="/watch?v=EBORaypI8VI" title="我的男孩第16集預告">
    我的男孩第16集預告
    </a>
    <span class="accessible-description" id="description-id-188415"> - 播放時間：0:29。</span>
</h3>
<div class="yt-lockup-byline ">
    <a class="yt-uix-sessionlink spf-link " data-sessionlink="itct=CAoQ3DAYGyITCNChtLf1tNoCFYFmKgodaEcJ5CjpHg" href="/channel/UCvgNKuXdfNGNaEKoG4nNwRA">
        snsdexo love
    </a>
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
