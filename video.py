import yt_dlp


def download_video(url):
    ydl_opts = {
        'ignoreerrors': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
