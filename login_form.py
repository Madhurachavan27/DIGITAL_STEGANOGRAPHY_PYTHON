import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import subprocess

def Starting_interface():
    subprocess.Popen(['python','C:/Users/madhura/OneDrive/Documents/DIGITAL STEGANOGRAPHY/Starting_interface.py'])

# Database initialization
conn = sqlite3.connect('user_credentials.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, email TEXT, password TEXT)''')
conn.commit()

# Function to create a new account
def register():
    def add_user():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if not email or '@' not in email:
            messagebox.showerror("Error", "Please enter a valid email address")
            return

        try:
            c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                      (username, email, password))
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully!")
            register_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("1000x1000")
    register_window.configure(bg="#e3f4f1")

    register_label = tk.Label(register_window, text="Register User", font=("DejaVu Serif", "28", "bold "), fg="black", bg="#e3f4f1")
    register_label.pack(pady=10)

    username_label = tk.Label(register_window, text="Username:",  font=("DejaVu Serif", "10"), fg="black", bg="#e3f4f1")
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()

    email_label = tk.Label(register_window, text="Email:",  font=("DejaVu Serif", "10"), fg="black", bg="#e3f4f1")
    email_label.pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack()

    password_label = tk.Label(register_window, text="Password:",  font=("DejaVu Serif", "10"), fg="black", bg="#e3f4f1")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()

    register_button = ttk.Button(register_window, text="Register", command=add_user, style="Pink.TButton")
    register_button.pack(pady=10)

    

# Function to handle forget password
def forgot_password():
    def reset_password():
        username = username_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()

        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        old_password = c.fetchone()[0]

        if new_password == old_password:
            messagebox.showerror("Error", "New password must be different from the old password")
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        c.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
        messagebox.showinfo("Success", "Password reset successfully!")
        forgot_password_window.destroy()

    forgot_password_window = tk.Toplevel(root)
    forgot_password_window.title("Forgot Password")
    forgot_password_window.geometry("1000x1000")
    forgot_password_window.configure(bg="#e3f4f1")

    forgot_password_label = tk.Label(forgot_password_window, text="Forgot Password", font=("DejaVu Serif", "28", "bold "), fg="black", bg="#e3f4f1")
    forgot_password_label.pack(pady=10)

    username_label = tk.Label(forgot_password_window, text="Username:",  font=("DejaVu Serif", "10"), fg="black", bg="#e3f4f1")
    username_label.pack()
    username_entry = tk.Entry(forgot_password_window)
    username_entry.pack()

    new_password_label = tk.Label(forgot_password_window, text="New Password:",  font=("DejaVu Serif", "10"), fg="black", bg="#e3f4f1")
    new_password_label.pack()
    new_password_entry = tk.Entry(forgot_password_window, show="*")
    new_password_entry.pack()

    confirm_password_label = tk.Label(forgot_password_window, text="Confirm Password:",  font=("DejaVu Serif", "10"), fg="black", bg="#e3f4f1")
    confirm_password_label.pack()
    confirm_password_entry = tk.Entry(forgot_password_window, show="*")
    confirm_password_entry.pack()

    reset_button = ttk.Button(forgot_password_window, text="Reset Password", command=reset_password, style="Pink.TButton")
    reset_button.pack(pady=10)

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()

    if user:
        Starting_interface()
    else:
        messagebox.showerror("Error", "Invalid username or password")

root = tk.Tk()
root.title("Login")
root.geometry("1000x1000")
root.configure(bg="#e3f4f1")

title_label = tk.Label(root, text="Digital Steganography", font=("DejaVu Serif", "28", "bold "), fg="black", bg="#e3f4f1")
title_label.pack(pady=20)

login_label = tk.Label(root, text="Login User", font=("DejaVu Serif", "20", "bold "), fg="black", bg="#e3f4f1")
login_label.pack(pady=10)

username_label = tk.Label(root, text="Username:", font=("DejaVu Serif", "10"), fg="black", bg="#e3f4f1")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:", font=("DejaVu Serif", "10"), fg="black", bg="#e3f4f1")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = ttk.Button(root, text="Login", command=login,style="Pink.TButton")
login_button.pack(pady=10)

register_button = ttk.Button(root, text="Register", command=register, style="Pink.TButton")
register_button.pack()

forgot_password_button = ttk.Button(root, text="Forgot Password", command=forgot_password, style="Pink.TButton")
forgot_password_button.pack(pady=10)

style = ttk.Style()
style.configure("Pink.TButton", foreground="black", background="#1ABC9C", font=("Helvetica", 12), borderwidth=0)
style.map("Pink.TButton", background=[("active", "#16A085")])


root.mainloop()

conn.close()
