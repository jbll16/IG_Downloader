import tkinter as tk
import instaloader

def download_profile_media():
    # Your instaloader code for downloading media here
    pass

app = tk.Tk()
app.title("Instagram Downloader")
app.geometry("400x200")

username_label = tk.Label(app, text="Username:")
username_label.pack()

username_input = tk.Entry(app)
username_input.pack()

download_button = tk.Button(app, text="Download", command=download_profile_media)
download_button.pack()

app.mainloop()
