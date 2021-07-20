from pytube import YouTube, Playlist
# misc
import os, sys
#functions
import downloadVideo

FILE_PATH = r"C:\Users\Chris Massie\Google Drive\AudioVideoFiles"

FILE_PATH = input("Please paste the file path save location:")

FILENAME = "links.txt"

functionNumber = "0"
isAcceptableInput = False


while isAcceptableInput == False:
   print("0 - using playlist")
   print("1 - using link file")
   print("2 - using single video link")
   functionNumber = (input("Please type True or False:"))
   if (functionNumber == "0" or functionNumber == "1" or functionNumber == "2"):
      isAcceptableInput = True
      break
   else:
      print("Couldn't be bothered to bullet proof this, try again with 'True' or 'False'")

if (functionNumber == "0"):
   with open(FILENAME) as f:
      URLS = f.read().splitlines()
      for url in URLS:
         downloadVideo(url, FILE_PATH)
elif (functionNumber == "1"):
   PLAYLIST_URL = input("Please paste the playlist url:")
   playlist = Playlist(PLAYLIST_URL)
   print(playlist.video_urls)
   URLS = playlist.video_urls
   for url in URLS:
      downloadVideo(url, FILE_PATH)
elif (functionNumber == "2"):
   URL = input("Paste the video link:")
   downloadVideo(URL, FILE_PATH)









#TODO Only get one copy of the highest quality video
#TODO Only get one copy of the highest quality video
#TODO Merge Video and Audio together into new file and delete original video file to save space
#TODO Scrape video title down to only include 'a-z and 0-9' this will stop names breaking file paths





if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")