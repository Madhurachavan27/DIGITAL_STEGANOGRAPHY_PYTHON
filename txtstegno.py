import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog
from tkinter import filedialog, messagebox
import os


class TextSteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Steganography")
        self.root.geometry("1000x1000")
        self.root.configure(bg="#e3f4f1")

        self.title_label = tk.Label(root, text="Text Steganography", font=("DejaVu Serif", "28", "bold "), fg="black", bg="#e3f4f1")
        self.title_label.pack(pady=10)

        self.encode_button = ttk.Button(self.root, text="Encode Message", command=self.encode_message, style="Pink.TButton")
        self.encode_button.pack(pady=10)

        self.decode_button = ttk.Button(self.root, text="Decode Message", command=self.decode_message, style="Pink.TButton")
        self.decode_button.pack(pady=10)

        style = ttk.Style()
        style.configure("Pink.TButton", foreground="black", background="#1ABC9C", font=("Helvetica", 12), borderwidth=0)
        style.map("Pink.TButton", background=[("active", "#16A085")])

    def encode_message(self):
        text_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not text_file_path:
            messagebox.showerror("Error", "No text file selected.")
            return
        
        message = tkinter.simpledialog.askstring("Enter Message", "Enter the message to encode into the text file:")
        if not message:
            messagebox.showerror("Error", "No message entered.")
            return

        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not output_file_path:
            return

        try:
            with open(text_file_path, 'r') as text_file:
                original_text = text_file.read()

            # Combine the original text and encoded message
            encoded_text = original_text + "\n" + message

            # Write the encoded text to a new text file
            with open(output_file_path, 'w') as output_file:
                output_file.write(encoded_text)

            messagebox.showinfo("Success", "Message encoded successfully into text file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def decode_message(self):
        text_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not text_file_path:
            messagebox.showerror("Error", "No text file selected.")
            return

        try:
            with open(text_file_path, 'r') as text_file:
                lines = text_file.readlines()
                if len(lines) >= 2:
                    decoded_message = lines[-1].strip()
                else:
                    decoded_message = "No encoded message found in the file."

            messagebox.showinfo("Decoded Message", f"The decoded message is: {decoded_message}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextSteganographyApp(root)
    root.mainloop()
