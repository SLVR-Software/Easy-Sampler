from tkinter import *
from tkinter import filedialog
from helper import *
from tkinter.ttk import *
import threading

root = Tk()

root.title("Easy Sampler")
root.iconbitmap('img/record.ico')

def on_focusIn(event):
    YOUTUBE_URL.config(foreground='black')
    if YOUTUBE_URL.get() == "https://www.youtube.com/watch?v=00000000000":
        event.widget.delete(0, END)
    else:
        YOUTUBE_URL.config(foreground='black')
    canSample()

def on_focusOut(event):
    if YOUTUBE_URL.get().replace(" ","") == "":
        default_YOUTUBE_URL_TEXT.set("https://www.youtube.com/watch?v=00000000000")
        YOUTUBE_URL.config(foreground='gray')
    else:
        userText = YOUTUBE_URL.get().replace(" ","")
        event.widget.delete(0, END)
        default_YOUTUBE_URL_TEXT.set(userText)
    canSample()

def on_keyRelease(event):
    userText = YOUTUBE_URL.get().replace(" ","")
    event.widget.delete(0, END)
    default_YOUTUBE_URL_TEXT.set(userText)
    canSample()

def step():
    pass

def canSample():
    if((linkType(str((YOUTUBE_URL.get()))) == 'video') or (linkType(str((YOUTUBE_URL.get()))) == 'playlist') and YOUTUBE_URL.get() != 'https://www.youtube.com/watch?v=00000000000' and dirLabel['text'] != ""):
        sampleButton["state"] = NORMAL
    else:
        sampleButton["state"] = DISABLED

def clickSample():
    sampleButton["state"] = DISABLED
    if(linkType(str(YOUTUBE_URL.get())) == 'video'):
        totalVideosText = Label(text = "0/1")
        totalVideosText.grid(row=4,column=0)
    elif(linkType(str(YOUTUBE_URL.get())) == 'playlist'):
        hideSampleConfig()
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
                downloadVideo.downloadVideo(url,dirLabel['text'], False, root, progress)
                
                totalVideosText['text'] = (str(count) + "/" + str(len(URLS)))
            except Exception as e:
                print(e)
        totalVideosText.grid_forget()
        progress.grid_forget()
        showSampleConfig()

def hideSampleConfig():
    YOUTUBE_URL.grid_forget()
    dirSelectButton.grid_forget()
    dirLabel.grid_forget()
    sampleButton.grid_forget()

def showSampleConfig():
    YOUTUBE_URL.grid(row=0,column=0)
    dirSelectButton.grid(row=1,column=0)
    dirLabel.grid(row=2,column=0)
    sampleButton.grid(row=3,column=0)

def clickDirSelector():
    root.directory = filedialog.askdirectory()
    print(root.directory)
    dirLabel['text'] = root.directory
    canSample()

default_YOUTUBE_URL_TEXT = StringVar()
default_YOUTUBE_URL_TEXT.set("https://www.youtube.com/watch?v=00000000000")

YOUTUBE_URL = Entry(root, width=50, textvariable=default_YOUTUBE_URL_TEXT)
YOUTUBE_URL.bind("<FocusIn>", on_focusIn)
YOUTUBE_URL.bind("<FocusOut>", on_focusOut)
YOUTUBE_URL.bind("<KeyRelease>", on_keyRelease)
YOUTUBE_URL.grid(row=0, column=0)
YOUTUBE_URL.config(foreground='gray')
#YOUTUBE_URL.insert(0, "Enter the Youtube URL")

dirSelectButton = Button(root, text="Select Folder", command=clickDirSelector)
dirSelectButton.grid(row=1,column=0)

dirLabel = Label(text="")

dirLabel.grid(row=2,column=0)

sampleButton = Button(root, text="Sample", command=clickSample)
sampleButton.grid(row=3,column=0)
sampleButton["state"] = DISABLED






root.mainloop()

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")