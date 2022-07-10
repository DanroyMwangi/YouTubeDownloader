from pytube import YouTube


def progress(stream, chunk, remaining):
    print(((file_size-remaining)*100)/file_size)


link = input('Enter the link to the video you want:')

youtubeVideo = YouTube(link,on_progress_callback=progress)
hdStream = youtubeVideo.streams

print('The video has began downloading...')
global file_size
file_size = hdStream.filesize
print(hdStream)
#hdStream.download('C:\\Users\\danro\\Downloads\\Python Youtube Downloader')
print('Download complete.')
