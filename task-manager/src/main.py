from tkinter import *
from tkinter import messagebox
from taskmanager import TaskManager

def main():
    task_manager = TaskManager()

    root = Tk()
    root.title("Task Manager")

    Label(root, text="Task").grid(row=0, column=0)
    entry = Entry(root)
    entry.grid(row=0, column=1)

    listbox = Listbox(root)
    listbox.grid(row=1, column=0, columnspan=4)

    def list_tasks():
        listbox.delete(0, END)
        for id_, task in task_manager.view_tasks():
            listbox.insert(END, (id_, task))

    def add_task():
        task = entry.get()
        if task:
            task_manager.add_task(task)
            list_tasks()
            entry.delete(0,END)

    def delete_task():
        selected_task = listbox.curselection()
        if selected_task:
            task_id, _ = listbox.get(selected_task)
            task_manager.delete_task(task_id)
            list_tasks()

    Button(root, text="Add Task", command=add_task).grid(row=0, column=2)
    Button(root, text="Delete Task", command=delete_task).grid(row=0, column=3)

    list_tasks()
    root.mainloop()

if __name__ == "__main__":
    main()
