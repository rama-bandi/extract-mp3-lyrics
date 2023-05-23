
import os
from mutagen.id3 import ID3, ID3NoHeaderError

def extract_lyrics_from_mp3(mp3_file):
    try:
        audio = ID3(mp3_file)
        for frame_id, frame_value in audio.items():
            #print(f"{frame_id}")
            if frame_id.startswith("USLT"):
                print(f"{frame_value}")
                return frame_value.text
    except ID3NoHeaderError:
        return None

def print_all_tags(mp3_file):
    audio = ID3(mp3_file)
    for tag in audio:
        print(f"{tag}")
        print(f"{tag}: {audio[tag]}")

def save_lyrics_to_txt(track_title, lyrics, output_directory):
    file_name = f"{track_title}.txt"
    file_path = os.path.join(output_directory, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(lyrics)

def scan_directory(input_directory, output_directory):
    files = os.listdir(input_directory)
    for file in files:
        if file.endswith('.mp3'):
            mp3_file = os.path.join(input_directory, file)
            track_title = os.path.splitext(file)[0]
          #  print_all_tags(mp3_file)
            lyrics = extract_lyrics_from_mp3(mp3_file)
            if lyrics:
                print(f"{lyrics}")
                save_lyrics_to_txt(track_title, lyrics, output_directory)
                print(f"Lyrics extracted and saved for: {track_title}")
                print(f"File saved as: {track_title}.txt")
            else:
                print(f"No lyrics found for: {track_title}")

# Prompt for the input directory path (local directory)
input_directory = input("Enter the input directory path: ")

# Prompt for the output directory path
output_directory = input("Enter the output directory path: ")

# Call the function to scan the directories
scan_directory(input_directory, output_directory)
