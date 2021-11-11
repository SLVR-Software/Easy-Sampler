from tkinter import *
from tkinter import filedialog


root = Tk()

root.title("Easy Sampler")
root.iconbitmap('img/record.ico')

def on_focusIn(event):
    YOUTUBE_URL.config(foreground='black')
    if YOUTUBE_URL.get() == "https://www.youtube.com/watch?v=00000000000":
        event.widget.delete(0, END)
    else:
        YOUTUBE_URL.config(foreground='black')

def on_focusOut(event):
    if YOUTUBE_URL.get().replace(" ","") == "":
        default_YOUTUBE_URL_TEXT.set("https://www.youtube.com/watch?v=00000000000")
        YOUTUBE_URL.config(foreground='gray')
    else:
        userText = YOUTUBE_URL.get().replace(" ","")
        event.widget.delete(0, END)
        default_YOUTUBE_URL_TEXT.set(userText)


def clickSample():
    #PLAYLIST.processPlaylist(root.directory,False)
    pass

def clickDirSelector():
    root.directory = filedialog.askdirectory()
    print(root.directory)
    dirLabel['text'] = root.directory

default_YOUTUBE_URL_TEXT = StringVar()
default_YOUTUBE_URL_TEXT.set("https://www.youtube.com/watch?v=00000000000")

YOUTUBE_URL = Entry(root, width=50, textvariable=default_YOUTUBE_URL_TEXT)
YOUTUBE_URL.bind("<FocusIn>", on_focusIn)
YOUTUBE_URL.bind("<FocusOut>", on_focusOut)
YOUTUBE_URL.grid(row=0, column=0)
YOUTUBE_URL.config(foreground='gray')
#YOUTUBE_URL.insert(0, "Enter the Youtube URL")

dirSelectButton = Button(root, text="Folder", command=clickDirSelector)
dirSelectButton.grid(row=1,column=0)

dirLabel = Label(text="")

dirLabel.grid(row=2,column=0)

sampleButton = Button(root, text="Sample", command=clickSample)
sampleButton.grid(row=3,column=0)





root.mainloop()

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")