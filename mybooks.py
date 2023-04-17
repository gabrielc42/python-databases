#! python3
from tkinter import Tk, Button, Label, ScrollBar, ListBox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox


root = Tk()

root.title("My Books Database Application")
root.configure(background="light green")
root.geometry("850x500")
root.resizable(width=False,height=False)

title_label = ttk.Label(root, text = "Title", background="light green", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=24, textvariable=title_text)
title_entry.grid(row = 0, column = 1, sticky = W)

author_label = ttk.Label(root, text = "Author", background="light green", font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root, width=24, textvariable=author_text)
author_entry.grid(row = 0, column = 3, sticky = W)

isbn_label = ttk.Label(root, text = "ISBN", background="light green", font=("TkDefaultFont", 16))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width=24, textvariable=isbn_text)
isbn_entry.grid(row = 0, column = 5, sticky = W)

root.mainloop()