import os
import random

music_folder = r"D:\Music"

def play_random_song():
    songs = os.listdir(music_folder)

    if not songs:
        print("Music folder is empty.")
        return

    song = random.choice(songs)
    song_path = os.path.join(music_folder, song)

    print(f"Playing: {song}")
    os.startfile(song_path)
    return
