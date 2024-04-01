import tkinter as tk
import subprocess
from tkinter import PhotoImage

def open_login():
    # Add your code to open the image steganography window here
    subprocess.Popen(['python','C:/Users/madhura/OneDrive/Documents/DIGITAL STEGANOGRAPHY/login_form.py'])
    pass
class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.root.title('Digital Steganography')
        self.root.geometry('1000x1000')

        # Create a black canvas
        self.canvas = tk.Canvas(root, bg="#e3f4f1", width=1000, height=1000)
        self.canvas.pack()

        # Load splash screen image
        self.splash_image = PhotoImage(file="C:/Users/madhura/OneDrive/Documents/DIGITAL STEGANOGRAPHY/tmp/Digital steganography (1).png")
         # Place the image on the canvas
        self.canvas.create_image(500, 500, image=self.splash_image)
        # Call function to destroy splash screen after a few seconds
        self.root.after(2000, self.close_splash)


  
    def close_splash(self):
        # Destroy the splash screen window and open the main application window
        self.root.destroy()
        open_login()
       
class DigitalSteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Digital Steganography')
        self.root.geometry('1000x1000')
        SplashScreen()

        
def main():
    root = tk.Tk()
    splash = SplashScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
