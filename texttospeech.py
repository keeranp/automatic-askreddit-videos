from gtts import gTTS
import os
from mutagen.mp3 import MP3
import edge_tts

async def text_to_speech(content, max_length = 50):
    print("Turning text to speech")

    length = 0
    title_sound_path = os.path.join("assets", "sounds", "title.mp3")

    communicate = edge_tts.Communicate()
    with open(title_sound_path, 'wb') as title_sound:
        async for i in communicate.run(content["title"], voice='en-US-ChristopherNeural',):
            if i[2] is not None:
                title_sound.write(i[2])

    content["title_length"] = MP3(title_sound_path).info.length
    length += MP3(title_sound_path).info.length

    i = 0

    while length < max_length and i < len(content["comments"]):
        path = os.path.join("assets", "sounds", content["comments"][i]["id"] + ".mp3")

        with open(path, 'wb') as soundfile:
            async for j in communicate.run(content["comments"][i]["body"], voice='en-US-ChristopherNeural',):
                if j[2] is not None:
                    soundfile.write(j[2])

        content["comments"][i]["sound_length"] = MP3(path).info.length
        length += MP3(path).info.length
        i += 1
