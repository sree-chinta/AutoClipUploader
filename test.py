from tkinter import Tk
from tkinter.filedialog import askdirectory
# Prepare the video metadata

video_metadata = {
    "snippet": {
        "title": "My Awesome Video",
        "description": "This is an awesome video uploaded programmatically!",
        "tags": ["tag1", "tag2", "example"],
        "categoryId": "22"  # "22" is the category for "People & Blogs"
    },
    "status": {
        "privacyStatus": "public",  # Options: "public", "private", "unlisted"
    }
}


path = askdirectory(title="Select Folder")
print(path)
