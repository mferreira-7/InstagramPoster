from time import sleep
from instagrapi import Client
from ImageProcessor import processImage
from NewsDataHandler import getNewsFromBBC
from DescriptionCreator import createGeneratedDescription
import config
import random

cl = Client()
news_stories = getNewsFromBBC()
story_count = len(news_stories)
view_only = False

if view_only:
    for news_story in news_stories:
        print(news_story)
else:
    sleep(random.randint(1,85999))
    cl.login(config.username, config.password)

    for storyIdx in range(story_count):
        print(f"Posting Story {storyIdx+1}/{story_count}")
        try:
            processImage("images/" + news_stories[storyIdx][0], news_stories[storyIdx][2])
            storyDesc = createGeneratedDescription(news_stories[storyIdx][0], news_stories[storyIdx][1])
        except:
            continue

        media = cl.photo_upload(
            path = f"images/{news_stories[storyIdx][0]}.jpg",
            caption = storyDesc
        )

        print(f"Story {storyIdx+1} Posted \n")
        sleep(random.randint(1,3600))

print("All Stories Posted")
