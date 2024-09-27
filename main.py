import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from tkinter import Tk
from tkinter.filedialog import askdirectory


def getUserInput():
    # Prepare the video metadata
    title = input("Enter Video Title: ")
    description = input("Enter the description of the video: ")
    tags = list(input("Enter the tags: ").split())
    categoryId = 20
    privacy = input("Enter the video's privacy (public, private, unlisted): ")
    video_metadata = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": categoryId,  # "20" is the category for "Gaming"
        },
        "status": {
            "privacyStatus": privacy,  # Options: "public", "private", "unlisted"
        },
    }

    return video_metadata


def main():
    path = askdirectory(title="Select Folder")
    print(path)

    vid_metadata = getUserInput()
    print(vid_metadata)


if __name__ == "__main__":
    main()
