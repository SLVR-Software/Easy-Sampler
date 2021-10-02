from pytube import YouTube, Playlist
# misc
import os, sys
import json
#functions
import downloadVideo

CONFIG_FILE = 'config.txt'

#any config options could be setup here, just testing things out.
f = open ('config.json')
DATA = json.loads(f.read())

FILE_PATH = DATA['FILE_PATH']
print(FILE_PATH)

f.close()

if not os.path.exists(FILE_PATH):
    os.mkdir(FILE_PATH)
    # Create directory if it doesn't already exist
    # Useful for creating local directories for testing purposes

# FILE_PATH is where video and audio streams should be saved
# FILE_PATH can be relative or absolute
#with open(CONFIG_FILE, 'r') as config_file:
    #config_list = config_file.read().splitlines()
    #FILE_PATH = config_list[0].split('=')[1]
#FILE_PATH = input("Please paste the file path save location:")

FILENAME = "links.txt"

#FILE_PATH = r"C:\Users\Chris Massie\Google Drive\AudioVideoFiles"

functionNumber = "0"
isAcceptableInput = False

# TODO more robust input parsing, more command line arguments as seen fit
# right now we just support supplying a single argument (functionNumber)
if len(sys.argv) > 1: # Command-line arguments are supplied (filename counts as 1)
    if sys.argv[1] in ('0', '1', '2'):
        functionNumber = sys.argv[1]
        isAcceptableInput = True
    else:
        print('Invalid functionNumber argument')

while isAcceptableInput == False:
   print("0 - using link file")
   print("1 - using playlist link")
   print("2 - using single video link")
   functionNumber = (input("Please type a number and hit enter:"))
   if (functionNumber == "0" or functionNumber == "1" or functionNumber == "2"):
      isAcceptableInput = True
      break
   else:
      print("Couldn't be bothered to bullet proof this, try again with a number one through three")

if (functionNumber == "0"):
   try:
      with open(FILENAME) as f:
         URLS = f.read().splitlines()
         for url in URLS:
            downloadVideo.downloadVideo(url, FILE_PATH)
   except Exception as exception:
      print(exception)
elif (functionNumber == "1"):
   try:
      PLAYLIST_URL = input("Please paste the playlist url:")
      playlist = Playlist(PLAYLIST_URL)
      print(playlist.video_urls)
      URLS = playlist.video_urls
      for url in URLS:
         try:
            downloadVideo.downloadVideo(url, FILE_PATH)
         except Exception as e:
            print(e)
   except Exception as exception:
      print(exception)

elif (functionNumber == "2"):
   try:
      URL = input("Paste the video link:")
      downloadVideo.downloadVideo(URL, FILE_PATH)
   except Exception as exception:
      print(exception)

##TODO Only get one copy of the highest quality video
##TODO Only get one copy of the highest quality video
#TODO Merge Video and Audio together into new file and delete original video file to save space
##TODO Scrape video title down to only include 'a-z and 0-9' this will stop names breaking file paths

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")
