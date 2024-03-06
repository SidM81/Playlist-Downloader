from youtubesearchpython import VideosSearch
from pytube import YouTube


def main():
    f = open('Songs.txt','r')
    Lines = f.readlines()

    for line in Lines:
        videosSearch = VideosSearch(f'{line[2:-1]}',limit=1)
        yt = YouTube(f'{videosSearch.result()["result"][0]["link"]}')
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()