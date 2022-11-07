from gtts import gTTS
import os
from mutagen.mp3 import MP3

MAX_LENGTH = 50


def text_to_speech(content):
    print("Turning text to speech")


    length = 0
    title_sound = gTTS(content["title"], lang="en", slow=False)
    title_sound_path = os.path.join("assets","sounds", "title.mp3")
    title_sound.save(title_sound_path)
    length += MP3(title_sound_path).info.length

    i = 0

    while length < MAX_LENGTH and i < len(content["comments"]):
        tts = gTTS(content["comments"][i]["body"], lang="en", slow=False)
        path = os.path.join("assets","sounds", content["comments"][i]["id"] + ".mp3")
        tts.save(path)
        length += MP3(path).info.length
        i += 1
