import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, simpledialog

class VideoSteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Video Steganography')
        self.root.geometry('1000x1000')
        self.root.configure(bg='#e3f4f1')

        self.title_label = tk.Label(root, text="Video Steganography",font=("DejaVu Serif", "28", "bold "), bg='#e3f4f1', fg='black')
        self.title_label.pack(pady=20)
        
        
        self.encode_button = ttk.Button(root, text="Encode Video", command=self.encode_video, style="Pink.TButton")
        self.encode_button.pack(pady=20)
        
        self.decode_button = ttk.Button(root, text="Decode Video", command=self.decode_video,style="Pink.TButton")
        self.decode_button.pack(pady=20)

        style = ttk.Style()
        style.configure("Pink.TButton", foreground="black", background="#1ABC9C", font=("Helvetica", 12), borderwidth=0)
        style.map("Pink.TButton", background=[("active", "#16A085")])

    #@staticmethod
    def encode_video(self):
        video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
        if not video_path:
            return  # User canceled

         # Prompt user for message
        secret_message = simpledialog.askstring("Input", "Enter Message:")
        if not secret_message:
            return  # User canceled or no message entered

        output_path = filedialog.asksaveasfilename(filetypes=[("Video files", "*.mp4")], defaultextension=".mp4")
        if not output_path:
            return  # User canceled
        try:
            VideoSteganography.encode_video_to_file(video_path, secret_message, output_path)
            messagebox.showinfo("Success", "Video encoding completed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    
    def decode_video(self):
        video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
        if not video_path:
            return  # User canceled
        try:
            decoded_message = VideoSteganography.decode_video_from_file(video_path)
            if decoded_message:
                messagebox.showinfo("Decoded Message", f"The decoded message is: {decoded_message}")
            else:
                messagebox.showinfo("Decoded Message", "No hidden message found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
class VideoSteganography:
    @staticmethod
    def encode_video_to_file(input_path, message, output_path):
        try:
            video_capture = cv2.VideoCapture(input_path)
            if not video_capture.isOpened():
                raise ValueError("Failed to open video file.")

            fps = int(video_capture.get(cv2.CAP_PROP_FPS))
            frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
            width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Convert message to binary
            binary_message = ''.join(format(ord(char), '08b') for char in message)

            # Add end-of-message indicator to the binary message
            binary_message += '00000000'

            if len(binary_message) > frame_count:
              raise ValueError("Message is too long to be encoded in the video.")

              # Initialize video writer
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

             # Encode message into video frames
            frame_index = 0
            for i in range(0, len(binary_message), 3):
                ret, frame = video_capture.read()
                if not ret:
                  break

                pixel = frame[0, 0]  # Get the first pixel
                # Encode message bits into the least significant bits of the pixel values
                for j in range(3):
                    if frame_index < len(binary_message):
                        pixel[j] = pixel[j] & ~1 | int(binary_message[frame_index])
                        frame_index += 1

                frame[0, 0] = pixel  # Modify the first pixel
                video_writer.write(frame)

             # Write remaining frames
            while True:
                ret, frame = video_capture.read()
                if not ret:
                   break
                video_writer.write(frame)

             # Release resources
            video_capture.release()
            video_writer.release()
            messagebox.showinfo("Success", "Video encoding completed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    @staticmethod
    def decode_video_from_file(input_path):
         try:
           video_capture = cv2.VideoCapture(input_path)
           if not video_capture.isOpened():
              raise ValueError("Failed to open video file.")

        # Initialize decoded message
           decoded_message = ""
           bit_buffer = ""

        # Decode message from video frames
           while True:
              ret, frame = video_capture.read()
              if not ret:
                break

            # Get the first pixel from each frame
              pixel = frame[0, 0]

             # Extract the LSB from the color channels
              for j in range(3):
                bit_buffer += str(pixel[j] & 1)

                # If the bit buffer has accumulated 8 bits, convert them to a character
                if len(bit_buffer) == 8:
                    decoded_message += chr(int(bit_buffer, 2))
                    bit_buffer = ""  # Reset the bit buffer

        # Release video capture resource
           video_capture.release()

           return decoded_message

         except Exception as e:
           messagebox.showerror("Error", str(e))

    # If decoding fails, release video capture and return None
         video_capture.release()
         return None
              
def main():
    root = tk.Tk()
    app = VideoSteganographyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

