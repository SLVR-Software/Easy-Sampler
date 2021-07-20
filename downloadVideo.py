from pytube import YouTube, Playlist
# misc
import os, sys


def downloadVideo(url, FILE_PATH):
   video = YouTube(url)
   videoTitle = (video.title).replace(":","")
   STREAMS = video.streams
   SAVE_PATH = os.path.join(FILE_PATH, (video.title).replace(":","").replace("'",""))
   print(url)
   for stream in STREAMS:
      print("__________________________")
      print("Downloading... " + video.title)
      print("Details:")
      print(stream)
      isDownloaded = False
      if (stream.type == "video"):
         video.streams.get_by_itag(stream.itag).download(output_path=SAVE_PATH,filename_prefix=(stream.resolution+"-"+stream.type+"_"))
      elif (stream.type == "audio"):
         video.streams.get_by_itag(stream.itag).download(output_path=SAVE_PATH,filename_prefix=(stream.type+"_"))