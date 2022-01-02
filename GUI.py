from tkinter import *
from tkinter import filedialog
from helper import *
from tkinter.ttk import *
import threading
import sys
import spotipyUtils.spotipyHelper as spotitools


root = Tk()

root.title("Easy Sampler")
root.iconbitmap('img/record.ico')

def on_focusIn(event):
    YOUTUBE_URL.config(foreground='black')
    if YOUTUBE_URL.get() == "https://www.youtube.com/watch?v=00000000000":
        event.widget.delete(0, END)
    else:
        YOUTUBE_URL.config(foreground='black')
    canSampleYoutube()

def on_focusOut(event):
    if YOUTUBE_URL.get().replace(" ","") == "":
        default_YOUTUBE_URL_TEXT.set("https://www.youtube.com/watch?v=00000000000")
        YOUTUBE_URL.config(foreground='gray')
    else:
        userText = YOUTUBE_URL.get().replace(" ","")
        event.widget.delete(0, END)
        default_YOUTUBE_URL_TEXT.set(userText)
    canSampleYoutube()

def on_keyRelease(event):
    userText = YOUTUBE_URL.get().replace(" ","")
    event.widget.delete(0, END)
    default_YOUTUBE_URL_TEXT.set(userText)
    canSampleYoutube()

def step():
    pass

def canSampleYoutube():
    if((linkType(str((YOUTUBE_URL.get()))) == 'video') or (linkType(str((YOUTUBE_URL.get()))) == 'playlist') and YOUTUBE_URL.get() != 'https://www.youtube.com/watch?v=00000000000' and dirLabel['text'] != ""):
        youtube_sampleButton["state"] = NORMAL
    else:
        youtube_sampleButton["state"] = DISABLED

def clickSampleYoutube():
    youtube_sampleButton["state"] = DISABLED
    if(linkType(str(YOUTUBE_URL.get())) == 'video'):
        totalVideosText = Label(text = "0/1")
        totalVideosText.grid(row=4,column=0)
    elif(linkType(str(YOUTUBE_URL.get())) == 'playlist'):
        hideYoutubeSampleConfig()
        URLS = getPlaylist(YOUTUBE_URL.get())
        totalVideosText = Label(text="0/" + str(len(URLS)))
        totalVideosText.grid(row=4, column=0)
        count = 0
        for url in URLS:
            try:
                count += 1
                root.update()
                progress = Progressbar(root, orient = HORIZONTAL,
                                        length = 100, mode = 'determinate')
                progress.grid(row=5, column=0)
                print("outside")
                print(type(root))
                print(type(progress))
                downloadVideo.downloadVideo(url,youtube_dirLabel['text'], False, root, progress)
                
                totalVideosText['text'] = (str(count) + "/" + str(len(URLS)))
            except Exception as e:
                print(e)
        totalVideosText.grid_forget()
        progress.grid_forget()
        showYoutubeSampleConfig()

def hideYoutubeSampleConfig():
    YOUTUBE_URL.grid_forget()
    youtube_dirSelectButton.grid_forget()
    youtube_dirLabel.grid_forget()
    youtube_sampleButton.grid_forget()

def showYoutubeSampleConfig():
    YOUTUBE_URL.grid(row=0,column=0)
    youtube_dirSelectButton.grid(row=1,column=0)
    youtube_dirLabel.grid(row=2,column=0)
    youtube_sampleButton.grid(row=3,column=0)

def hideSpotifySampleConfig():
    spotify_playlist_menu.grid_forget()

def showSpotifySampleConfig():
    hideYoutubeSampleConfig()
    spotify_playlist_menu.grid(row=1, column=0)

def clickDirSelectorYoutube():
    root.directory = filedialog.askdirectory()
    print(root.directory)
    youtube_dirLabel['text'] = root.directory
    canSampleYoutube()

def spotifySelected():
    hideYoutubeSampleConfig()
    showSpotifySampleConfig()

def youtubeSelected():
    hideSpotifySampleConfig()
    showYoutubeSampleConfig()



#menu bar
menubar = Menu(root)
#open menu
openmenu = Menu(menubar, tearoff=0)
openmenu.add_command(label="Youtube Sampler", command=youtubeSelected)
openmenu.add_command(label="Spotify Sampler", command=spotifySelected)
menubar.add_cascade(label="Open", menu=openmenu)

#Youtube Form
default_YOUTUBE_URL_TEXT = StringVar()
default_YOUTUBE_URL_TEXT.set("https://www.youtube.com/watch?v=00000000000")

YOUTUBE_URL = Entry(root, width=50, textvariable=default_YOUTUBE_URL_TEXT)
YOUTUBE_URL.bind("<FocusIn>", on_focusIn)
YOUTUBE_URL.bind("<FocusOut>", on_focusOut)
YOUTUBE_URL.bind("<KeyRelease>", on_keyRelease)
YOUTUBE_URL.config(foreground='gray')
#YOUTUBE_URL.insert(0, "Enter the Youtube URL")

youtube_dirSelectButton = Button(root, text="Select Folder", command=clickDirSelectorYoutube)

youtube_dirLabel = Label(text="")

youtube_sampleButton = Button(root, text="Sample", command=clickSampleYoutube)
youtube_sampleButton["state"] = DISABLED
#End Youtube Form

spotify_playlists = spotitools.get_all_playlist()
spotify_playlistNames = []

for playlist in spotify_playlists:
    spotify_playlistNames.append(playlist['name'])

#fix for tkinter bug
spotify_playlistNames.insert(0, 'Select a Playlist')

spotify_playlistVariable = StringVar(root)

spotify_playlistVariable.set(spotify_playlistNames[0])

spotify_playlist_menu = OptionMenu(root, spotify_playlistVariable, *spotify_playlistNames)





root.config(menu=menubar)
root.mainloop()

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")