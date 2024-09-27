import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.discovery
import time
from googleapiclient.http import MediaFileUpload
from tkinter import Tk
from tkinter.filedialog import askdirectory
from googleapiclient.http import MediaFileUpload


def formatMetaData(folder, mtime, file):
    title = file[: len(file) - 4]
    description = str(folder) + " | Last modified on: " + str(mtime)
    tags = folder.replace(" ", "-")[0:500]
    categoryId = 20
    privacy = "unlisted"
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


def uploadVideo(path, video_metadata, credentials):
    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    # Define the media upload (the path to your video file)
    media = MediaFileUpload(path, chunksize=-1, resumable=True)

    # Make the request to upload the video
    request = youtube.videos().insert(
        part="snippet,status", body=video_metadata, media_body=media
    )

    # Execute the request
    response = request.execute()

    # Print the ID of the uploaded video
    print("Uploaded video ID:", response["id"])


def main():
    # Define the required scopes
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

    # Create a flow object using the client secrets JSON file
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json", SCOPES
    )

    # Run the local server to authenticate the user and get credentials
    credentials = flow.run_local_server(port=0)

    path = askdirectory(title="Select Folder")
    print(f"Folder selected: {path}")
    folder = os.path.basename(path).split("/")[-1]

    files = os.listdir()
    counter = 1
    for file in files:
        if not os.path.isdir(os.path.join(path, file)):

            if file[-4:] == ".mp4":
                mtime = os.path.getmtime(os.path.join(path, file))
                mtime = time.ctime(mtime)
                video_metadata = formatMetaData(folder, mtime, file)

                uploadVideo(os.path.join(path, file), video_metadata, credentials)

                print(f"{counter}: {video_metadata}\n")
                counter += 1

                if not os.path.exists(os.path.join(path, "Uploaded")):
                    os.makedirs("Uploaded")

                os.rename(
                    os.path.join(path, file), os.path.join(path, "Uploaded/" + file)
                )


if __name__ == "__main__":
    main()
