import youtube_dl
from pytube import Playlist


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'TuanNgoc-%(title)s.%(ext)s',  # output file naming format
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '384',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    playlist = Playlist('https://www.youtube.com/playlist?list=PLslbLkSgSFaM2lY5uXXwjevA2QJAwm4nP')  # playlist url
    result = ydl.download(playlist.video_urls)  # ydl.download([list of youtube urls])
