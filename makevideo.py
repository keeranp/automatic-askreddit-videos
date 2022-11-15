import os
from moviepy.editor import *
import random
from random import randrange


def make_video(content, max_length=50):
    os.makedirs(os.path.join("assets", "videos", content["id"]), exist_ok=True)
    with open(os.path.join("assets", "videos", content["id"], "title.txt"), "w") as f:
        f.write(content["title"])
        f.write(" #reddit #redditreadings #redditstories #reddit_tiktok")

    title_audioclip = AudioFileClip(os.path.join("assets", "sounds", "title.mp3"))

    title_clip = ImageClip(os.path.join("assets", "images", "title.png"))
    title_clip = title_clip.set_duration(content["title_length"])
    title_clip = title_clip.set_audio(title_audioclip)
    title_clip = title_clip.resize(width=900)
    clips = [title_clip]

    i = 0
    length = content["title_length"]

    while length < max_length and i < len(content["comments"]):
        comment_audioclip = AudioFileClip(
            os.path.join("assets", "sounds", content["comments"][i]["id"] + ".mp3")
        )

        image_clip = ImageClip(
            os.path.join("assets", "images", content["comments"][i]["id"] + ".png")
        )
        image_clip = image_clip.set_duration(content["comments"][i]["sound_length"])
        image_clip = image_clip.set_audio(comment_audioclip)
        image_clip = image_clip.resize(width=900)

        clips.append(image_clip)

        length += content["comments"][i]["sound_length"]
        i += 1

    background_clip = VideoFileClip(
        os.path.join("assets", "backgrounds", "minecraft.mp4")
    )
    random_time = randrange(180, int(background_clip.duration) - int(length))
    background_clip = background_clip.subclip(random_time, random_time + length)
    background_clip = background_clip.crop(x1=656, width=608)
    background_clip = background_clip.resize((1080, 1920))

    screenshots = concatenate_videoclips(clips, method="compose")
    video = CompositeVideoClip([background_clip, screenshots.set_position("center")])
    video = video.set_fps(24)

    video.write_videofile(os.path.join("assets", "videos", content["id"], "video.mp4"))
