###open youtube video

import os
import webbrowser

# checks if url file exists. if not makes it

if not os.path.isfile("youtube_video.txt"):
    print('creating "youtube_video.txt"...')

with open("youtube_video.txt", "w") as file:
    file.write("https://www.youtube.com/watch?v=1x8kEFV02lY&ab_channel=SATUNES%2CSNIPPETS%26LEAKS")

#function for playing video
def play():
    with open("youtube_video.txt") as file:
        vides = file.readlines()
    webbrowser.open(vides[0])
    
    
