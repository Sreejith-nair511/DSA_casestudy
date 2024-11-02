import tkinter as tk
from tkinter import filedialog, messagebox
from pygame import mixer
from PIL import Image, ImageTk
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Playlist System")
        self.root.geometry("600x500")
        self.root.configure(bg='black')  # Change the background color to magenta

        mixer.init()
        self.playlist = []
        self.covers = []
        self.current_song_index = 0

        self.title = tk.Label(self.root, text="Music Playlist System", font=("Comic Sans MS", 20), bg='magenta').pack()

        self.add_btn = tk.Button(self.root, text="Add Song", command=self.add_song, font=("Comic Sans MS", 12), bg='white').pack()
        self.play_btn = tk.Button(self.root, text="Play Song", command=self.play_song, font=("Comic Sans MS", 12), bg='blue').pack()
        self.prev_btn = tk.Button(self.root, text="Previous Song", command=self.prev_song, font=("Comic Sans MS", 12), bg='purple').pack()
        self.next_btn = tk.Button(self.root, text="Next Song", command=self.next_song, font=("Comic Sans MS", 12), bg='yellow').pack()

        self.song_list = tk.Listbox(self.root, font=("Comic Sans MS", 10), bg='white')
        self.song_list.pack(fill="both", expand=True)

        self.cover_label = tk.Label(self.root, bg='blue')
        self.cover_label.pack(pady=10)

        self.song_title = tk.Label(self.root, font=("Comic Sans MS", 12), bg='black')
        self.song_title.pack(anchor='center')


    def add_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.playlist.append(file_path)
            self.song_list.insert(tk.END, os.path.basename(file_path))

            cover_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
            if cover_path:
                self.covers.append(cover_path)
            else:
                self.covers.append(None)

    def play_song(self):
        if self.playlist:
            mixer.music.load(self.playlist[self.current_song_index])
            mixer.music.play()
            self.display_cover()
            self.display_title()

    def prev_song(self):
        if self.playlist:
            self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
            self.play_song()

    def next_song(self):
        if self.playlist:
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            self.play_song()

    def display_cover(self):
        cover_path = self.covers[self.current_song_index]
        if cover_path:
            img = Image.open(cover_path)
            img = img.resize((150, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.cover_label.config(image=photo)
            self.cover_label.image = photo
            self.cover_label.pack(anchor='center')  # Center the image
        else:
            self.cover_label.config(image='')

    def display_title(self):
        song_name = os.path.basename(self.playlist[self.current_song_index])
        self.song_title.config(text=song_name, anchor='center')


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
