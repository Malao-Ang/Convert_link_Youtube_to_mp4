
from tkinter import *
import tkinter as tk
from moviepy.editor import *
import string
from pytube import YouTube
from tkinter import messagebox

root = tk.Tk()
root.geometry('400x120')
root.configure(bg='black') 
root.iconbitmap('mine.png')

def ConvertMp4():
    link = linkInput.get()
    try: 
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()
        messagebox.showinfo(title="Sucess", message="Convert to mp4 alrady")
    except Exception as e:
        messagebox.showerror("Had something wrong", "Please check your link.")
    
    
    
linkInput = tk.StringVar()
root.title("Youtube to mp4")

titleLabel = tk.Label(root,text="Link Youtube",fg = "black")
linkLabel = tk.Entry(root,textvariable = linkInput,width = 50)
convertBtn = tk.Button(root,text="Convert to mp4",command = ConvertMp4)

titleLabel.grid(row = 0,padx=150,pady=2)
linkLabel.grid(row = 1,padx=0,pady=5)
convertBtn.grid(row = 2,padx=150,pady=10)
root.mainloop()
quit()