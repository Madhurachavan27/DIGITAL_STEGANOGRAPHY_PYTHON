import tkinter as tk
from tkinter import ttk
import subprocess


def open_image_steganography():
    # Add your code to open the image steganography window here
    subprocess.Popen(['python','C:/Users/madhura/OneDrive/Documents/DIGITAL STEGANOGRAPHY/ImgStegno.py'])
    pass

def open_video_steganography():
    # Add your code to open the video steganography window here
    subprocess.Popen(['python','C:/Users/madhura/OneDrive/Documents/DIGITAL STEGANOGRAPHY/VdoStegno.py'])
    pass

def open_audio_steganography():
    # Add your code to open the audio steganography window here
    subprocess.Popen(['python','C:/Users/madhura/OneDrive/Documents/DIGITAL STEGANOGRAPHY/AudioStegnowav.py'])
    pass

def open_login():
    # Add your code to open the image steganography window here
    subprocess.Popen(['python','C:/Users/madhura/OneDrive/Documents/DIGITAL STEGANOGRAPHY/login_form.py'])
    pass


def logout():
    # Add your code to handle logout here, for example, destroy the current window and open the login window
    global root  # Access the global root variable
    root.destroy()
    open_login()

def main():
    global root
    root = tk.Tk()
    root.title("Digital Steganography")
    root.geometry("1000x1000")
    root.configure(bg="#e3f4f1")

    title_label = tk.Label(root, text="Digital Steganography", font=("DejaVu Serif", "28", "bold "), fg="black", bg="#e3f4f1")
    title_label.pack(pady=20)

    image_button = ttk.Button(root, text="Image Steganography", command=open_image_steganography, style="Pink.TButton")
    image_button.pack(pady=10)
    

    video_button = ttk.Button(root, text="Video Steganography", command=open_video_steganography, style="Pink.TButton")
    video_button.pack(pady=10)

    audio_button = ttk.Button(root, text="Audio Steganography", command=open_audio_steganography, style="Pink.TButton")
    audio_button.pack(pady=10)

    logout_button = ttk.Button(root, text="Logout", command=logout, style="Pink.TButton")
    logout_button.place(relx=1.0, rely=0.0, anchor=tk.NE, x=-10, y=10)  # Place button in the top-right corner with padding


    style = ttk.Style()
    style.configure("Pink.TButton", foreground="black", background="#1ABC9C", font=("Helvetica", 12), borderwidth=0)
    style.map("Pink.TButton", background=[("active", "#16A085")])
    root.mainloop()

if __name__ == "__main__":
    main()
