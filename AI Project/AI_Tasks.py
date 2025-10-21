from tkinter import *
from tkinter import ttk

def submit():
    name = name_textbox.get().strip()
    sid = sid_textbox.get().strip()

    for widget in root.grid_slaves(row=8, column=1):
        widget.destroy()

    if not name:
        error_label = Label(root, text="Error: Name cannot be empty", fg="red")
        error_label.grid(row=8, column=1)
        return
    elif not name.isalpha():
        error_label = Label(root, text="Error: Name must contain only letters", fg="red")
        error_label.grid(row=8, column=1)
        return

    sid_int = int(sid)
    task_textbox.config(state=NORMAL)
    if name and sid:
        if sid_int % 2 == 0:
            task_textbox.delete(0, END)
            task_textbox.insert(0, "To complete task A: Display an image by selection.")
        if sid_int % 2 == 1:
            task_textbox.delete(0, END)
            task_textbox.insert(0, "To complete task B: Display all images then shuffle them.")

    success_label = Label(root, text="Login Successful!", fg="green")
    success_label.grid(row=8, column=1)

root = Tk()
root.title("AI Project completed by Ng Tsz Yin (20307097)")
root.geometry("500x200")

name_label = Label(root, text="Name:")
name_textbox = Entry(root, width=50, fg="#000", bg="#fff")

sid_label = Label(root, text="Student ID:")
sid_textbox = Entry(root, width=50, fg="#000", bg="#fff")

task_label = Label(root, text="Your Task:")
task_textbox = Entry(root, width=50, fg="#000", bg="#fff")
task_textbox.config(state=DISABLED)

submit_btn = Button(root, width=10, text="Submit", command=submit)
exit_btn = Button(root, width=15, text="Exit Program", command=root.quit)

name_label.grid(row=0, column=1)
name_textbox.grid(row=1, column=1)
sid_label.grid(row=2, column=1)
sid_textbox.grid(row=3, column=1)
task_label.grid(row=4, column=1)
task_textbox.grid(row=5, column=1)
submit_btn.grid(row=6, column=1)
exit_btn.grid(row=7, column=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()