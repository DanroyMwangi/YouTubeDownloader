from pytube import YouTube
import os
from dotenv import load_dotenv
load_dotenv()

global videoSize


def progress(stream, chunk, remaining):
    percent = ((videoSize-remaining)*100)/videoSize
    print("Completed:%0.00f%s" % (percent, '%'))


link = input('Enter the link to the video you want:')
resolution = int(input('Choose the quality you want.\n1. 144p\n2. 360p\n3. 720p\n4. 1080p\n'))
youtubeVideo = YouTube(link, on_progress_callback=progress)
hdStream = youtubeVideo.streams

#https://www.youtube.com/watch?v=9txjIvXafvc

match resolution:
    case 1:
        video = hdStream.filter(resolution='144p', progressive=True).first()
        videoSize = video.filesize
        fileName=video.title+' 144p.'+video.subtype
        print('%s has began downloading...' % fileName)
        video.download(os.getenv('DOWNLOAD_PATH'), fileName)
        print('Download complete.')
    case 2:
        video = hdStream.filter(resolution='360p', progressive=True).first()
        videoSize = video.filesize
        fileName = video.title + ' 360p.' + video.subtype
        print('%s has began downloading...' % fileName)
        video.download(os.getenv('DOWNLOAD_PATH'), fileName)
        print('Download complete.')
    case 3:
        video = hdStream.filter(resolution='720p', progressive=True).first()
        videoSize = video.filesize
        fileName = video.title + ' 720p.' + video.subtype
        print('%s has began downloading...' % fileName)
        video.download(os.getenv('DOWNLOAD_PATH'), fileName)
        print('Download complete.')
    case 4:
        video = hdStream.filter(resolution='1080p', progressive=True).first()
        videoSize = video.filesize
        fileName = video.title + ' 1080p.' + video.subtype
        print('%s has began downloading...' % fileName)
        video.download(os.getenv('DOWNLOAD_PATH'), fileName)
        print('Download complete.')