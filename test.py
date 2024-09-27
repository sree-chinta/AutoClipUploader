from tkinter import Tk
from tkinter.filedialog import askdirectory

path = askdirectory(title="Select Folder")
print(path)
