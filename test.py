from tkinter import Tk
from tkinter.filedialog import askdirectory

import os

# Prepare the video metadata
title = input("Enter Video Title: ")
description = input("Enter the description of the video: ")
tags = list(input("Enter the tags: ").split())
categoryId = input("Enter the category: ")
privacy = input("Enter the video's privacy (public, private, unlisted): ")
video_metadata = {
    "snippet": {
        "title": title,
        "description": description,
        "tags": tags,
        "categoryId": categoryId,  # "22" is the category for "People & Blogs"
    },
    "status": {
        "privacyStatus": privacy,  # Options: "public", "private", "unlisted"
    },
}

path = askdirectory(title="Select Folder")
print(path)

if not os.path.exists(os.path.join(path, "Uploaded")):
    os.makedirs(os.path.join(path, "Uploaded"))
