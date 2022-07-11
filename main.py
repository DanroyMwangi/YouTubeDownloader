import pytube
from pytube import YouTube
import os
from dotenv import load_dotenv
load_dotenv()

global videoSize
pytube.request.default_range_size = 9437184


def progress(stream, chunk, remaining):
    percent = ((videoSize-remaining)*100)/videoSize
    print("Completed:%0.00f%s" % (percent, '%'))


link = input('Enter the link to the video you want:')
youtubeVideo = YouTube(link, on_progress_callback=progress)
hdStream = youtubeVideo.streams
fileType = int(input('Do you want:\n1. Audio only\n2. Video only\n3. Both video and audio'))

match fileType:
    case 1:
        audio = hdStream.filter(only_audio=True, progressive=True).get_audio_only()
        audioSize = audio.filesize
        fileName = audio.title + ' audio' + audio.subtype
        print('%s has began downloading...' % fileName)
        audio.download(os.getenv('DOWNLOAD_PATH'), fileName)
        print('Download complete.')
    case 2:
        resolution = int(input('Choose the quality you want.\n1. 144p\n2. 360p\n3. 720p\n4. 1080p\n5. Best quality\n6. Lowest quality\n'))
        # https://www.youtube.com/watch?v=9txjIvXafvc
        match resolution:
            case 1:
                video = hdStream.filter(only_video=True, resolution='144p', progressive=True).first()
                videoSize = video.filesize
                fileName = video.title + ' 144p.' + video.subtype
                print('%s has began downloading...' % fileName)
                video.download(os.getenv('DOWNLOAD_PATH'), fileName)
                print('Download complete.')
            case 2:
                video = hdStream.filter(only_video=True,resolution='360p', progressive=True).first()
                videoSize = video.filesize
                fileName = video.title + ' 360p.' + video.subtype
                print('%s has began downloading...' % fileName)
                video.download(os.getenv('DOWNLOAD_PATH'), fileName)
                print('Download complete.')
            case 3:
                video = hdStream.filter(only_video=True,resolution='720p', progressive=True).first()
                videoSize = video.filesize
                fileName = video.title + ' 720p.' + video.subtype
                print('%s has began downloading...' % fileName)
                video.download(os.getenv('DOWNLOAD_PATH'), fileName)
                print('Download complete.')
            case 4:
                video = hdStream.filter(only_video=True,resolution='1080p', progressive=True).first()
                videoSize = video.filesize
                fileName = video.title + ' 1080p.' + video.subtype
                print('%s has began downloading...' % fileName)
                video.download(os.getenv('DOWNLOAD_PATH'), fileName)
                print('Download complete.')
            case 5:
                video = hdStream.filter(only_video=True,progressive=True).get_highest_resolution()
                videoSize = video.filesize
                fileName = video.title + ' HD.' + video.subtype
                print('%s has began downloading...' % fileName)
                video.download(os.getenv('DOWNLOAD_PATH'), fileName)
                print('Download complete.')
            case 6:
                video = hdStream.filter(only_video=True,progressive=True).get_lowest_resolution()
                videoSize = video.filesize
                fileName = video.title + ' Lowest.' + video.subtype
                print('%s has began downloading...' % fileName)
                video.download(os.getenv('DOWNLOAD_PATH'), fileName)
                print('Download complete.')
    case 3:
        resolution = int(input('Choose the quality you want.\n1. 144p\n2. 360p\n3. 720p\n4. 1080p\n5. Best quality\n6. Lowest quality\n'))
        # https://www.youtube.com/watch?v=9txjIvXafvc
        match resolution:
            case 1:
                video = hdStream.filter(resolution='144p', progressive=True).first()
                videoSize = video.filesize
                fileName = video.title + ' 144p.' + video.subtype
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
            case 5:
                video = hdStream.filter(progressive=True).get_highest_resolution()
                videoSize = video.filesize
                fileName = video.title + ' HD.' + video.subtype
                print('%s has began downloading...' % fileName)
                video.download(os.getenv('DOWNLOAD_PATH'), fileName)
                print('Download complete.')
            case 6:
                video = hdStream.filter(progressive=True).get_lowest_resolution()
                videoSize = video.filesize
                fileName = video.title + ' Lowest.' + video.subtype
                print('%s has began downloading...' % fileName)
                video.download(os.getenv('DOWNLOAD_PATH'), fileName)
                print('Download complete.')