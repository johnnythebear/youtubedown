#!python3
from tkinter import *
from pytube import YouTube, Playlist
import pyperclip

def download_video(path="."):
    try:
        video = YouTube(pyperclip.paste()).streams.first()
        video.download(path)
        text.delete(0.0, END)
        text.insert(END, "Done.")
    except:
        text.delete(0.0, END)
        text.insert(END, "It's not a YouTube video link! Maybe a playlist?")

def download_playlist(path="."):
    try:
        playlist = Playlist(pyperclip.paste())
        playlist.download_all(path)
        text.delete(0.0, END)
        text.insert(END, "Done.")
    except:
        text.delete(0.0, END)
        text.insert(END, "It's not a YouTube playlist link! Maybe a single video?")

window = Tk()
window.title("YouTube downloader")
label = Label(window, text="Copy a YouTube video or playlist link to the clipboard!", width=50, height=2)
button_vid = Button(window, text="Download video!", command=download_video)
button_pla = Button(window, text="Download playlist!", command=download_playlist)
text = Text(window, width=50, height=2)

##label.pack()
##button_vid.pack(side="left", padx=4, pady=4)
##button_pla.pack(side="right", padx=4, pady=4)
##text.pack()
label.grid(row=1, column=2, columnspan=2)
button_vid.grid(row=2, column=1, columnspan=2)
button_pla.grid(row=2, column=3, columnspan=2)
text.grid(row=3, column=2, columnspan=2)
window.mainloop()
