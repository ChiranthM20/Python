import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ------------------ Task Class ------------------ #
class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = "Pending"

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.title} | Priority: {self.priority} | Due: {self.due_date.date()} | Status: {self.status}"


# ------------------ Task Manager Class ------------------ #
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()


# ------------------ GUI Application ------------------ #
class TaskApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Task Manager / To-Do App")
        self.root.geometry("600x400")

        # Entry fields
        self.title_entry = tk.Entry(root, width=30)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(root, text="Task Title:").grid(row=0, column=0)

        self.priority_entry = tk.Entry(root, width=30)
        self.priority_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(root, text="Priority (High/Medium/Low):").grid(row=1, column=0)

        self.due_entry = tk.Entry(root, width=30)
        self.due_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Label(root, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Delete Task", command=self.delete_task).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Mark Complete", command=self.complete_task).grid(row=3, column=2, pady=10)

        # Task list display
        self.task_listbox = tk.Listbox(root, width=80, height=15)
        self.task_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.manager.tasks):
            self.task_listbox.insert(tk.END, f"{i}. {task}")

    def add_task(self):
        title = self.title_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_entry.get()

        if not title or not priority or not due_date:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            self.manager.add_task(title, priority, due_date)
            self.refresh_list()
            self.title_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
            self.due_entry.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.manager.delete_task(index)
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.manager.mark_task_complete(index)
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark complete.")


# ------------------ Run App ------------------ #
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
