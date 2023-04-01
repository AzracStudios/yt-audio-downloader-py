from pytube import YouTube
from moviepy.editor import *
import os
import time 


def main():
    songI = 0
    startTime = time.time()

    links = list(open("./links.txt", "r"))
    for link in links:
        try:
            vid = YouTube(link)
            startTime = time.time()

            print(f"\n******************** DOWNLOADING VIDEO AT INDEX {songI} ********************\n")
            print(f"Video Title: {vid.title}\nVideo Author: {vid.author}\nVideo Views: {vid.views}\nVideo Upload Date: {vid.publish_date}\n\nDownloading as MP4...")
            vid.streams.first().download("./out", filename=f"{vid.title}.mp4")

            print("Download Completed!")
            print("Extracting Audio")

            inp = VideoFileClip(f"./out/{vid.title}.mp4")
            out = inp.audio

            print("Saving Audio")

            out.write_audiofile(f"./out/{vid.title}.mp3")

            print("Removing MP4...")
            os.remove(f"./out/{vid.title}.mp4")

            print("Completed!")

            endTime = time.time()

            print(f"\nTime Elapsed: {endTime - startTime} seconds\n*************************************************************************\n")

        except Exception as e:
            print(f"Couldn't Download Video: {e}")
        
        finally:
            songI += 1

    endTime = time.time()
    s = "songs" if len(links) == 1 else "song"
    print(f"Downloaded {len(links)} {s} in {endTime - startTime} seconds")

main()