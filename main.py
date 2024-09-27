from tkinter import Tk
from tkinter.filedialog import askdirectory


def main():
    path = askdirectory(title="Select Folder")
    print(path)


if __name__ == "__main__":
    main()
