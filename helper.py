import promptlib
import os

def promptUserForDirectory():
    prompter = promptlib.Files()
    dir = prompter.dir()
    #file = prompter.file()
    print(dir)
    audioDir = os.path.join(dir, "AudioFiles")
    videoDir = os.path.join(dir, "VideoFiles")
    if not os.path.isdir(audioDir):
        os.mkdir(audioDir)
    if not os.path.isdir(videoDir):
        os.mkdir(videoDir)
    return dir

def linkType(link):
    if link != None and "https://www.youtube.com/playlist?list=" in link:
        return "playlist"
    elif "https://www.youtube.com/watch?v=" in link:
        return "video"

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")

