#needs debugging
from pytube import Youtube
import wget
"""
pseudo code:

ask for a link to download
    if connect on youtube
        ok
    else
        raise error and ask again
ask for where to store the video
    store the link
connect to the adress
    
launch scrapping
clean scrap
send a message to the user with a local link for the video
"""

link = input("Entrer le lien de la vidéo a telecharger")
try: 
    video = Youtube(link)
    wget.download(Youtube(link))
except pytube.exceptions.PytubeError:
    print(f"Video {video.title} unavaialable.")