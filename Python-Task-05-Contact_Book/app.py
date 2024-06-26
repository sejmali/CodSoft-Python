import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Initialize the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

contacts = {}

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

def add_contact():
    popup_window("Add Contact", add_contact_action)

def add_contact_action(popup, name, phone, email):
    if name and phone and email:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts()
        refresh_contact_list()
    popup.destroy()

def view_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        contact = contacts[selected_contact]
        messagebox.showinfo("View Contact", f"Name: {selected_contact}\nPhone: {contact['phone']}\nEmail: {contact['email']}")

def update_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        popup_window("Update Contact", update_contact_action, selected_contact, contacts[selected_contact]['phone'], contacts[selected_contact]['email'])

def update_contact_action(popup, name, phone, email):
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if name and phone and email:
        contacts.pop(selected_contact)
        contacts[name] = {"phone": phone, "email": email}
        save_contacts()
        refresh_contact_list()
    popup.destroy()

def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        response = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {selected_contact}?")
        if response:
            contacts.pop(selected_contact)
            save_contacts()
            refresh_contact_list()

def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact)

def popup_window(title, action, name="", phone="", email=""):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("500x400")
    popup.configure(bg="#1e1e1e")
    popup.grab_set()
    
    def on_close():
        popup.grab_release()
        popup.destroy()
    
    popup.protocol("WM_DELETE_WINDOW", on_close)
    
    title_label = tk.Label(popup, text=title, font=("Helvetica", 16), bg="#1e1e1e", fg="white")
    title_label.pack(pady=10)
    
    name_label = tk.Label(popup, text="Name:", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
    name_label.pack(pady=5)
    name_entry = tk.Entry(popup, font=("Helvetica", 14), width=40)
    name_entry.pack(pady=5)
    name_entry.insert(0, name)
    
    phone_label = tk.Label(popup, text="Phone:", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
    phone_label.pack(pady=5)
    phone_entry = tk.Entry(popup, font=("Helvetica", 14), width=40)
    phone_entry.pack(pady=5)
    phone_entry.insert(0, phone)
    
    email_label = tk.Label(popup, text="Email:", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
    email_label.pack(pady=5)
    email_entry = tk.Entry(popup, font=("Helvetica", 14), width=40)
    email_entry.pack(pady=5)
    email_entry.insert(0, email)
    
    button_frame = tk.Frame(popup, bg="#1e1e1e")
    button_frame.pack(pady=20)
    
    ok_button = tk.Button(button_frame, text="OK", font=("Helvetica", 14), width=10, command=lambda: action(popup, name_entry.get(), phone_entry.get(), email_entry.get()))
    ok_button.grid(row=0, column=0, padx=10)
    
    cancel_button = tk.Button(button_frame, text="Cancel", font=("Helvetica", 14), width=10, command=popup.destroy)
    cancel_button.grid(row=0, column=1, padx=10)

# Load contacts from file
load_contacts()

# Create UI elements
title_label = tk.Label(root, text="Contact Book", font=("Helvetica", 24), bg="#1e1e1e", fg="white")
title_label.pack(pady=20)

contact_listbox = tk.Listbox(root, font=("Helvetica", 14), width=40, height=10)
contact_listbox.pack(pady=10)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", font=("Helvetica", 14), width=15, command=add_contact)
add_button.grid(row=0, column=0, padx=5, pady=5)

view_button = tk.Button(button_frame, text="View Contact", font=("Helvetica", 14), width=15, command=view_contact)
view_button.grid(row=0, column=1, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Contact", font=("Helvetica", 14), width=15, command=update_contact)
update_button.grid(row=1, column=0, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Contact", font=("Helvetica", 14), width=15, command=delete_contact)
delete_button.grid(row=1, column=1, padx=5, pady=5)

quit_button = tk.Button(root, text="Quit", font=("Helvetica", 14), width=15, command=root.quit)
quit_button.pack(pady=20)

# Refresh contact list on startup
refresh_contact_list()

# Start the main loop
root.mainloop()
