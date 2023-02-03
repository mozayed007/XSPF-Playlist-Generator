import argparse
import os
import xml.etree.ElementTree as ET

def create_xspf_playlist(folder_path, playlist_file):
    # Create the root element of the XSPF playlist file
    root = ET.Element("playlist", version="1", xmlns="http://xspf.org/ns/0/")
    tracklist = ET.SubElement(root, "trackList")

    # Sort the videos in the folder by name
    videos = sorted(os.listdir(folder_path))

    # Add each video to the tracklist
    for video in videos:
        track = ET.SubElement(tracklist, "track")
        location = ET.SubElement(track, "location").text = "file://" + os.path.join(folder_path, video)

    # Write the XSPF playlist to a file
    tree = ET.ElementTree(root)
    tree.write(playlist_file, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an XSPF playlist file that sorts the videos in a folder by name.")
    parser.add_argument("folder", type=str, help="The path to the folder containing the videos.")
    parser.add_argument("playlist", type=str, help="The path to the XSPF playlist file.")
    args = parser.parse_args()

    create_xspf_playlist(args.folder, args.playlist)