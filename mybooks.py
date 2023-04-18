#! python3
from tkinter import Scrollbar, Tk, Button, Label, ScrollBar, ListBox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox


root = Tk() # Creates application window

root.title("My Books Database Application") # Title to application window
root.configure(background="light green") # Background color to app window
root.geometry("850x500") # Size for app window
root.resizable(width=False,height=False) # Prevents app window resizing

# Label and entry widgets

title_label = ttk.Label(root, text = "Title", background="light green", font=("TkDefaultFont", 16))
title_label.grid(row = 0, column = 0, sticky = W)
title_text = StringVar()
title_entry = ttk.Entry(root, width = 24, textvariable = title_text)
title_entry.grid(row = 0, column = 1, sticky = W)

author_label = ttk.Label(root, text = "Author", background = "light green", font = ("TkDefaultFont", 16))
author_label.grid(row = 0, column = 2, sticky = W)
author_text = StringVar()
author_entry = ttk.Entry(root, width = 24, textvariable = author_text)
author_entry.grid(row = 0, column = 3, sticky = W)

isbn_label = ttk.Label(root, text = "ISBN", background = "light green", font = ("TkDefaultFont", 16))
isbn_label.grid(row = 0, column = 4, sticky = W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width = 24, textvariable = isbn_text)
isbn_entry.grid(row = 0, column = 5, sticky = W)

# input buttons

add_btn = Button(root, text = "Add Book", bg = "blue", fg = "white", font = "helvetica 10 bold", command = "")
add_btn.grid(row = 0, column = 6, sticky = W)

# listbox displays data

list_bx = ListBox(root, height = 16, width = 40, font = "helvetica 13", bg = "light blue")
list_bx.grid(row = 3, column = 1, columnspan = 14, sticky = W + E, pady = 40, padx = 15)

# scrollbar

scroll_bar = Scrollbar(root)
scroll_bar.grid(row = 1, column = 8, rowspan = 14, sticky = W)

list_bx.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = list_bx.yview)

# button widgets

modify_btn = Button(root, text="Modify Record", bg="purple", fg="white", font="helvetica 10 bold", command="")
modify_btn.grid(row=15, column=4)

delete_btn = Button(root, text="Delete Record", bg="red", fg="white", font="helvetica 10 bold", command="")
delete_btn.grid(row=15, column=5)

view_btn = Button(root, text="View all records", bg="black", fg="white", font="helvetica 10 bold", command="")
view_btn.grid(row=15, column=1)

clear_btn = Button(root, text="Clear Screen", bg="maroon", fg="white", font="helvetica 10 bold", command="")
clear_btn.grid(row=15, column=2)

exit_btn = Button(root, text="Exit Application", bg="blue", fg="white", font="helvetica 10 bold", command="")
exit_btn.grid(row=15, column=3)



root.mainloop() # runs app until exit