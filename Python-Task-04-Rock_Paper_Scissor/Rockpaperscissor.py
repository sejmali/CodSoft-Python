import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("600x600")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Function to center the window
def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

# Center the window after it has been drawn
root.update_idletasks()
center_window(root)

# Symbols for Rock, Paper, Scissors
symbols = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Function to determine the winner
def determine_winner(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        scores["user"] += 1
    else:
        result = "Computer wins!"
        scores["computer"] += 1

    user_choice_label.config(text=f"Your choice: {symbols[user_choice]}")
    computer_choice_label.config(text=f"Computer's choice: {symbols[computer_choice]}")
    result_label.config(text=result)
    update_scores()

def update_scores():
    user_score_label.config(text=f"User Score: {scores['user']}")
    computer_score_label.config(text=f"Computer Score: {scores['computer']}")

def quit_game():
    root.quit()

# Initialize scores
scores = {"user": 0, "computer": 0}

# Create UI elements
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 24), bg="#1e1e1e", fg="white")
title_label.pack(pady=20)

user_choice_label = tk.Label(root, text="Your choice: ", font=("Helvetica", 16), bg="#1e1e1e", fg="white")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=("Helvetica", 16), bg="#1e1e1e", fg="white")
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#1e1e1e", fg="white")
result_label.pack(pady=10)

user_score_label = tk.Label(root, text="User Score: 0", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
user_score_label.pack()

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
computer_score_label.pack()

button_frame = tk.Frame(root, bg="#1e1e1e", width=500)
button_frame.pack(pady=20, padx=20)

button_style = {"font": ("Helvetica", 20), "width": 10, "height": 2, "bg": "#3e3e3e", "fg": "white", "activebackground": "#575757", "activeforeground": "white"}

rock_button = tk.Button(button_frame, text=symbols["rock"], command=lambda: determine_winner("rock"), **button_style)
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = tk.Button(button_frame, text=symbols["paper"], command=lambda: determine_winner("paper"), **button_style)
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = tk.Button(button_frame, text=symbols["scissors"], command=lambda: determine_winner("scissors"), **button_style)
scissors_button.grid(row=0, column=2, padx=10, pady=5)

quit_button = tk.Button(root, text="Quit", command=quit_game, font=("Helvetica", 14), width=15, height=2, bg="#3e3e3e", fg="white", activebackground="#575757", activeforeground="white")
quit_button.pack(pady=20)

# Start the main loop
root.mainloop()
