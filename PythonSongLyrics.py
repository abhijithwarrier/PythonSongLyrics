# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO SEARCH FOR AND GET THE LYRICS OF THE USER ENTERED SONG USING lyricsgenius LIBRARY
# IN THIS YOU CAN SEARCH FOR THE LYRICS BY ENTERING THE SONG NAME OR BOTH SONG NAME AND ARTIST NAME.
#
# lyricsgenius provides a simple interface to the song, artist, and lyrics data stored on Genius.com.
# Using this library you can convienently access content on Genius.com And much more using public API.
# Genius.com is a fun website. Genius hosts a bunch of song lyrics and lets users highlight and
# annotate passages with interpretations, explanations, and references.
# You need to get the ACCESS TOKEN by signing up and creating an api at http://genius.com/api-clients
#
# The module can be installed using the command - pip install lyricsgenius

# Importing necessary packages
import tkinter as tk
import lyricsgenius as lg
import tkinter.scrolledtext as sb_text
from tkinter import *

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    songLabel = Label(root, text="SONG : ", bg="lightblue4")
    songLabel.grid(row=0, column=0, padx=10, pady=5)
    songEntry = Entry(root, width=25, bg='azure3', textvariable=song)
    songEntry.grid(row=0, column=1, padx=10, pady=5)

    searchButton = Button(root, text="SEARCH", command=searchFor)
    searchButton.grid(row=0, column=2, padx=10, pady=5, rowspan=2)

    artistLabel = Label(root, text="ARTIST : ", bg="lightblue4")
    artistLabel.grid(row=1, column=0, padx=10, pady=5)
    artistEntry = Entry(root, width=25, bg='azure3', fg="blue", textvariable=artist)
    artistEntry.grid(row=1, column=1, padx=10, pady=5)

    lyricsLabel = Label(root, text="LYRICS : ", bg="lightblue4")
    lyricsLabel.grid(row=2, column=0, padx=10, pady=5)
    root.lyricsText = sb_text.ScrolledText(root, width=40, height=25, bg='azure3')
    root.lyricsText.grid(row=3, column=0, rowspan=5, columnspan=3, padx=10, pady=5)
    # Making Text Widget uneditable by setting state parameter of config() to DISABLED
    root.lyricsText.config(state=DISABLED, font = "Calibri 15", wrap="word")

# Defining the searchFor() to get the lyrics of entered song
def searchFor():
    # Storing the user-entered song and artist in the respective variables
    i_song = song.get()
    i_artist = artist.get()
    # Initializing the API by passing the ACCESS TOKEN obtained from GENIUS API
    genius = lg.Genius('ibXs8vCEhGcpgUkNGeywhOIGAF2hZs2cxy_IeqLkmNv_ojZZ3AT1iDPgaDgrvnno')
    # Searching for the lyrics of the song using the search_song() method.
    # Just song name can be passed or both song name and artist name can be passed
    lyrics = genius.search_song(i_song, i_artist)
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.lyricsText.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.lyricsText.delete('1.0', END)
    # Displaying lyrics of the user entered song in the lyricsText Widget
    root.lyricsText.insert("end", lyrics.lyrics)
    # Making Widget uneditable again after the displaying list of news from feed
    root.lyricsText.config(state=DISABLED)

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize
# & disabling the resizing property
root.title("PythonSongLyrics")
root.geometry("442x590")
root.config(background="lightblue4")
root.resizable(False, False)
# Creating the tkinter variables
song = StringVar()
artist = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
