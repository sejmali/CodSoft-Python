import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")
        self.root.config(bg="#282C34")
        self.center_window(400, 350)
        
        # Create and place the labels, entry, and buttons with enhanced styles
        self.label = tk.Label(root, text="Enter the desired password length:", bg="#282C34", fg="#61AFEF", font=("Helvetica", 12))
        self.label.pack(pady=10)
        
        self.length_entry = tk.Entry(root, font=("Helvetica", 12))
        self.length_entry.pack(pady=5)
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg="#61AFEF", fg="#282C34", font=("Helvetica", 12, "bold"))
        self.generate_button.pack(pady=10)
        
        self.password_label = tk.Label(root, text="", bg="#282C34", fg="#98C379", font=("Helvetica", 12, "bold"))
        self.password_label.pack(pady=10)
        
        self.copy_button = tk.Button(root, text="Copy Password", command=self.copy_password, bg="#98C379", fg="#282C34", font=("Helvetica", 12, "bold"))
        self.copy_button.pack(pady=10)
        self.copy_button.config(state=tk.DISABLED)  # Initially disable the button

    def center_window(self, width, height):
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate the position x and y coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                raise ValueError("Password length should be at least 4.")
            password = self.create_password(length)
            self.password_label.config(text=f"Generated Password: {password}")
            self.copy_button.config(state=tk.NORMAL)  # Enable the button after generating a password
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def create_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Ensure the password has at least one of each character type
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        
        # Fill the rest of the password length with random characters
        password += random.choices(characters, k=length-4)
        
        # Shuffle the password list to ensure randomness
        random.shuffle(password)
        
        return ''.join(password)

    def copy_password(self):
        password = self.password_label.cget("text").split(": ")[1]  # Extract the password from the label text
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Password Copied", "The password has been copied to the clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
