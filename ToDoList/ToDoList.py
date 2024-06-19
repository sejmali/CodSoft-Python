import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json, os
from datetime import datetime

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do-List App by Sejal Mali")

        window_width = 600
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.minsize(500, 450)
        style = Style(theme="flatly")
        style.configure("Custom.TEntry", foreground="gray")

        icon_path = "E:\CodeHub\python_pgming\CodSoft\ToDoList\icon.png" 
        self.icon_image = tk.PhotoImage(file=icon_path)
        self.iconphoto(False, self.icon_image)

        self.task_input = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custom.TEntry")
        self.task_input.pack(pady=5)

        self.task_input.insert(0, "Enter task...")
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        self.task_input.bind("<FocusOut>", self.restore_placeholder)

        ttk.Label(self, text="Priority:").pack(pady=5)
        self.priority = ttk.Combobox(self, values=["Low", "Medium", "High"], state="readonly")
        self.priority.current(0)
        self.priority.pack(pady=5)

        ttk.Label(self, text="Deadline (YYYY-MM-DD):").pack(pady=5)
        self.deadline = ttk.Entry(self, font=("TkDefaultFont", 16), width=30)
        self.deadline.pack(pady=5)

        ttk.Button(self, text="Add Task", command=self.add_task).pack(pady=5)

        columns = ("#1", "#2", "#3")
        self.task_list = ttk.Treeview(self, columns=columns, show="headings")
        self.task_list.heading("#1", text="Task")
        self.task_list.heading("#2", text="Priority")
        self.task_list.heading("#3", text="Deadline")

        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.task_list.bind("<ButtonRelease-1>", self.on_task_select)

        ttk.Button(self, text="Mark as Done", style="success.TButton", command=self.task_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete Task", style="danger.TButton", command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)
        ttk.Button(self, text="View Stats", style="info.TButton", command=self.view_statistics).pack(side=tk.BOTTOM, pady=10)

        self.load_tasks()

    def view_statistics(self):
        done_count = 0
        total_count = len(self.task_list.get_children())
        for task in self.task_list.get_children():
            if "done" in self.task_list.item(task, "tags"):
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task = self.task_input.get()
        priority = self.priority.get()
        deadline = self.deadline.get()

        if not task or task == "Enter task...":
            messagebox.showinfo("Input Error", "Please enter a task to add.")
        else:
            try:
                if deadline:
                    datetime.strptime(deadline, "%Y-%m-%d")
                self.task_list.insert("", tk.END, values=(task, priority, deadline), tags=("pending",))
                self.task_input.delete(0, tk.END)
                self.deadline.delete(0, tk.END)
                self.priority.current(0)
                self.save_tasks()
            except ValueError:
                messagebox.showinfo("Input Error", "Please enter a valid date in YYYY-MM-DD format.")

    def task_done(self):
        selected_item = self.task_list.selection()
        if selected_item:
            self.task_list.item(selected_item, tags=("done",))
            self.save_tasks()

    def delete_task(self):
        selected_item = self.task_list.selection()
        if not selected_item:
            messagebox.showinfo("No Task Selected", "Please select a task to delete.")
        else:
            self.task_list.delete(selected_item)
            self.save_tasks()

    def on_task_select(self, event):
        selected_item = self.task_list.selection()
        if selected_item:
            item = self.task_list.item(selected_item)
            task = item['values'][0]
            priority = item['values'][1] 
            deadline = item['values'][2]
            self.task_input.delete(0, tk.END)
            self.task_input.insert(0, task)
            self.priority.set(priority)
            self.deadline.delete(0, tk.END)
            self.deadline.insert(0, deadline)

    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter task...":
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="TEntry")

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter task...")
            self.task_input.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            filepath = os.path.join(os.path.dirname(__file__), "tasks.json")
            with open(filepath, "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert("", tk.END, values=(task["text"], task["priority"], task["deadline"]), tags=("pending",))
        except FileNotFoundError:
            pass

    def save_tasks(self):
        data = []
        for task in self.task_list.get_children():
            values = self.task_list.item(task, "values")
            status = self.task_list.item(task, "tags")[0]
            data.append({"text": values[0], "priority": values[1], "deadline": values[2], "status": status})
        filepath = os.path.join(os.path.dirname(__file__), "tasks.json")
        with open(filepath, "w") as f:
            json.dump(data, f)

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()
