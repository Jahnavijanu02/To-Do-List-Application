import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
import requests
from io import BytesIO

def add_task():
    title = title_entry.get()
    description = description_entry.get()
    task = f"Title: {title}\nDescription: {description}"
    task_list.insert(tk.END, task)
def remove_task():
    selected_task = task_list.get(tk.ACTIVE)
    task_list.delete(tk.ACTIVE)
def mark_as_read():
    selected_item = task_list.curselection()  # Get the selected task
    if selected_item:
        task_index = selected_item[0]  # Get the index of the selected task
        task_list.itemconfig(task_index, {'bg': 'green'})  # Change the background color to green



app = tk.Tk()

app.geometry("400x400")

url = "https://images3.alphacoders.com/126/1261816.jpg"
response = requests.get(url)
img_data = response.content
img = Image.open(BytesIO(img_data))
photo = ImageTk.PhotoImage(img)
label1 = Label(app, image=photo)
label1.place(x=0, y=0)

app.title("To-Do List Application")
main_title=tk.Label(app,text="To Do list Application",font="times 20",bg="#73628A",foreground="white")
main_title.pack()
title_label = tk.Label(app, text="Title:",font="times 20")
title_label.pack()
title_label.place(x=730,y=50)

title_entry = tk.Entry(app,font="times 20",width=60,bg="light pink")
title_entry.pack()
title_entry.place(x=350,y=80)

description_label = tk.Label(app, text="Description:",font="times 20")
description_label.pack()
description_label.place(x=700,y=130)

description_entry = tk.Entry(app,font="times 20",width=60,bg="light pink")
description_entry.pack()
description_entry.place(x=350,y=160)

add_button = tk.Button(app, text="Add Task", font="times 20",activebackground="green",activeforeground="white",command=add_task)
add_button.pack()
add_button.place(x=350,y=250)

remove_button = tk.Button(app, text="Remove Task", font="times 20",activebackground="red",activeforeground="white",command=remove_task)
remove_button.pack()
remove_button.place(x=670,y=250)

mark_as_read_button = tk.Button(app, text="Mark as Read", font="times 20", activebackground="blue", activeforeground="white", command=mark_as_read)
mark_as_read_button.pack()
mark_as_read_button.place(x=1025,y=250)

task_list = tk.Listbox(app,font="times 20",height=10,width=60,bg="light pink")
task_list.pack()
task_list.place(x=350,y=380)
app.mainloop()