import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog
from tkinter import filedialog, messagebox
import os
import wave


class AudioSteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Steganography")
        self.root.geometry("1000x1000")
        self.root.configure(bg="#e3f4f1")

        self.title_label = tk.Label(root, text="Audio Steganography",font=("DejaVu Serif", "28", "bold "), fg="black", bg="#e3f4f1")
        self.title_label.pack(pady=20)

        self.encode_button = ttk.Button(self.root, text="Encode Text", command=self.encode_text,style="Pink.TButton")
        self.encode_button.pack(pady=10)

        self.decode_button = ttk.Button(self.root, text="Decode Text", command=self.decode_text,style="Pink.TButton")
        self.decode_button.pack(pady=10)

        style = ttk.Style()
        style.configure("Pink.TButton", foreground="black", background="#1ABC9C", font=("Helvetica", 12), borderwidth=0)
        style.map("Pink.TButton", background=[("active", "#16A085")])

    def encode_text(self):
        audio_file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if not audio_file_path:
            messagebox.showerror("Error", "No audio file selected.")
            return
        
        text_to_encode = tkinter.simpledialog.askstring("Enter Text", "Enter the text to encode into the audio file:")
        if not text_to_encode:
            messagebox.showerror("Error", "No text entered.")
            return

        output_file_path = filedialog.asksaveasfilename(defaultextension=".wav")
        if not output_file_path:
            return


        try:
            with wave.open(audio_file_path, 'rb') as audio_file:
                audio_data = audio_file.readframes(audio_file.getnframes())

            # Encode text into LSB of audio data
            encoded_audio_data = self.encode_message(audio_data, text_to_encode)

            # Write the encoded audio data to a new WAV file
            with wave.open(output_file_path, 'wb') as output_file:
                output_file.setparams(audio_file.getparams())
                output_file.writeframes(encoded_audio_data)

            messagebox.showinfo("Success", "Text encoded successfully into audio file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def decode_text(self):
        audio_file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if not audio_file_path:
            messagebox.showerror("Error", "No audio file selected.")
            return

        try:
            with wave.open(audio_file_path, 'rb') as audio_file:
                audio_data = audio_file.readframes(audio_file.getnframes())

            # Decode text from LSB of audio data
            decoded_text = self.decode_message(audio_data)

            messagebox.showinfo("Decoded Text", f"The decoded text is: {decoded_text}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def encode_message(self, audio_data, message):
        encoded_data = bytearray(audio_data)
        message_length = len(message)

        # Encode message length in the first 32 bits
        for i in range(32):
            encoded_data[i] = (encoded_data[i] & 254) | ((message_length >> i) & 1)

        # Encode each character of the message
        for i, char in enumerate(message):
            for j in range(8):
                encoded_data[32 + i * 8 + j] = (encoded_data[32 + i * 8 + j] & 254) | ((ord(char) >> j) & 1)

        return bytes(encoded_data)

    def decode_message(self, audio_data):
        message_length = 0

        # Decode message length from the first 32 bits
        for i in range(32):
            message_length |= (audio_data[i] & 1) << i

        decoded_message = ''

        # Decode each character of the message
        for i in range(message_length):
            char_value = 0
            for j in range(8):
                char_value |= (audio_data[32 + i * 8 + j] & 1) << j
            decoded_message += chr(char_value)

        return decoded_message
    


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioSteganographyApp(root)
    root.mainloop()
