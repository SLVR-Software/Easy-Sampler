from pytube import YouTube, Playlist
# misc
import os, sys

FILE_PATH = r"C:\Users\Chris Massie\Google Drive\AudioVideoFiles"
print(FILE_PATH)

FILENAME = "links.txt"


isPlaylist = "False"
isAcceptableInput = False

while isAcceptableInput == False:
   print("True = using playlist")
   print("False = using link file")
   isPlaylist = (input("Please type True or False:"))
   if (isPlaylist == "True" or isPlaylist == "False"):
      isAcceptableInput = True
      break
   else:
      print("Couldn't be bothered to bullet proof this, try again with 'True' or 'False'")

if (isPlaylist == "False"):
   with open(FILENAME) as f:
      URLS = f.read().splitlines()
elif (isPlaylist == "True"):
   PLAYLIST_URL = input("Please paste the playlist url:")
   playlist = Playlist(PLAYLIST_URL)
   print(playlist.video_urls)
   URLS = playlist.video_urls

for url in URLS:
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

#TODO Only get one copy of the highest quality video
#TODO Only get one copy of the highest quality video
#TODO Merge Video and Audio together into new file and delete original video file to save space
#TODO Scrape video title down to only include 'a-z and 0-9' this will stop names breaking file paths





if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")