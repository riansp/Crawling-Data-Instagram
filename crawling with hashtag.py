from instalooter.looters import ProfileLooter
from instalooter.looters import HashtagLooter
from instalooter.looters import PostLooter
from datetime import datetime, timedelta
from time import gmtime
from time import strftime
import re
import os

Hastag = ("ppkm")

looter = HashtagLooter(Hastag)        
_baseurl = "https://www.instagram.com/explore/tags/"

date = datetime.today()
HOURS_THRESHOLD = 12

for media in looter.medias():
    info = looter.get_post_info(media['shortcode'])
    print(info)
    time = media.get('taken_at_timestamp') or media['date']
    create_date = strftime("%Y-%m-%d %H:%M:%S", gmtime(time))
    date_time_obj = datetime.strptime(create_date, '%Y-%m-%d %H:%M:%S')
    duration = date - date_time_obj
    duration_in_s = duration.total_seconds() 
    hours = abs(divmod(duration_in_s, 3600)[0])
    print(hours)
    print(date)
    print(date_time_obj)
    if hours > HOURS_THRESHOLD:
        break
    owner = info['owner']['username']
    print('Owner Post :', owner)
    edgeslen = len(info["edge_media_to_caption"]["edges"])
    if edgeslen < 1:
        continue
    caption = info["edge_media_to_caption"]["edges"][0]["node"]["text"]
    print('Caption :', caption)
    like = info['edge_media_preview_like']['count']
    print('Total Likes :', like)
    comment = info['edge_media_to_parent_comment']['count']
    print('Total Comment :', comment)
    for comments in info['edge_media_to_parent_comment']['edges']:
        comm_username = comments['node']['owner']['username']
        print('User Comment :', comm_username)
        comm_text  = comments['node']['text']
        print('Comment :', comm_text)
    print('')
    post_url = info.get('shortcode')
    print('Url Post :', 'https://www.instagram.com/p/'+ post_url)
    media = looter.get_post_info(media['shortcode'])
    link = media.get('video_url') or media.get('display_url')
    print('Url Picture/Video :', link)
    
