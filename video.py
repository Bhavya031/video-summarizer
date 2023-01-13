import os
import yt_dlp as youtube_dlp
import re


def remove_special_chars(string):
    return re.sub(r'[^\w\s]', '', string)


def download_video(url):
    ydl = youtube_dlp.YoutubeDL()
    info = ydl.extract_info(url, download=False)
    title = remove_special_chars(info['title'])
    extension = info['ext']
    ydl_opts = {
        'ignoreerrors': True,
        'outtmpl': os.path.join('audio/', f'{title}.%(ext)s'),
    }
    with youtube_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return os.path.join('audio/', f'{title}.{extension}'), title
