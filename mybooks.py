#! python3
from tkinter import Scrollbar, Tk, Button, Label, ScrollBar, ListBox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox


root = Tk()

root.title("My Books Database Application")
root.configure(background="light green")
root.geometry("850x500")
root.resizable(width=False,height=False)

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

add_btn = Button(root, text = "Add Book", bg = "blue", fg = "white", font = "helvetica 10 bold", command = "")
add_btn.grid(row = 0, column = 6, sticky = W)

list_bx = ListBox(root, height = 16, width = 40, font = "helvetica 13", bg = "light blue")
list_bx.grid(row = 3, column = 1, columnspan = 14, sticky = W + E, pady = 40, padx = 15)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row = 1, column = 8, rowspan = 14, sticky = W)

list_bx.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = list_bx.yview)

root.mainloop()