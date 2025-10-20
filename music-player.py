import pygame
import os
import time

# --- Configuration ---
# Set the path to your folder containing MP3 files
music_dir = 'path/to/your/music/folder'  # **CHANGE THIS PATH**

# --- Setup ---
pygame.mixer.init()

# Get the playlist (list all files with a .mp3 extension)
try:
    all_files = os.listdir(music_dir)
    # Filter for MP3 files and construct full path
    playlist = [os.path.join(music_dir, f) for f in all_files if f.endswith('.mp3')]
except FileNotFoundError:
    print(f"Error: Directory not found at {music_dir}")
    playlist = []

if not playlist:
    print("No MP3 files found in the directory. Please check the 'music_dir' path.")
else:
    print(f"Found {len(playlist)} songs in the playlist.")
    current_song_index = 0
    
    # --- Playback Function ---
    def play_next_song():
        global current_song_index
        
        if current_song_index < len(playlist):
            song = playlist[current_song_index]
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            print(f"Now playing: {os.path.basename(song)}")
            current_song_index += 1
        else:
            print("Playlist finished.")
            pygame.mixer.music.stop()

    # Start playing the first song
    play_next_song()

    # --- Main Loop to Monitor Playback ---
    # The music playback runs in the background. We need a loop to check when a song ends.
    # Note: This simple method uses a basic time-based check. For a more robust solution 
    # (especially in GUI apps), you would use pygame events (like set_endevent).
    try:
        while pygame.mixer.music.get_busy() or current_song_index < len(playlist):
            # Check if music is finished but there are still songs left
            if not pygame.mixer.music.get_busy() and current_song_index < len(playlist):
                play_next_song()
            
            # Sleep briefly to reduce CPU usage
            time.sleep(1) 
    except KeyboardInterrupt:
        print("\nPlayback interrupted by user.")
    finally:
        pygame.mixer.music.stop()
        pygame.quit()
        print("Music player closed.")
