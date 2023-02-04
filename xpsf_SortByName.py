import argparse
import os
import xml.etree.ElementTree as ET

def create_xspf_playlist(folder_path, playlist_file):
    # Supported video and audio file formats
    extensions = (".mp4", ".mkv", ".flv", ".avi", ".wmv", ".mov", ".mp3", ".m4a", ".flac", ".wav")

    # Create the root element of the XSPF playlist file
    root = ET.Element("playlist", version="1", xmlns="http://xspf.org/ns/0/")
    tracklist = ET.SubElement(root, "trackList")

    # Sort the videos and audio files in the folder by name
    files = sorted(os.listdir(folder_path), key=lambda x: (int(''.join([i for i in x if i.isdigit()])), x))

    # Add each video and audio file to the tracklist
    for file in files:
        if os.path.splitext(file)[1].lower() in extensions:
            track = ET.SubElement(tracklist, "track")
            location = ET.SubElement(track, "location").text = "file://" + os.path.join(folder_path, file)

    # Write the XSPF playlist to a file
    tree = ET.ElementTree(root)
    tree.write(playlist_file, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an XSPF playlist file that only includes video and audio files and sorts them by name.")
    parser.add_argument("folder", type=str, help="The path to the folder containing the files.")
    parser.add_argument("playlist", type=str, help="The path to the XSPF playlist file.")
    args = parser.parse_args()

    create_xspf_playlist(args.folder, args.playlist)