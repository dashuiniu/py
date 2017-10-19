#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @auth 大水牛 ad190929@163.com

import json
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

def calculate(*args):
    try:
        value = json.loads(feet_entry.get(0.0, END));
        obj = json.dumps(value, indent=4, check_circular=FALSE, ensure_ascii=False)
        meters_entry.delete(0.0, END)
        meters_entry.insert(INSERT, obj)
    except ValueError:
        pass

# -**----------------  TK -------------#
root = Tk()
root.title("Json Online")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="JSON TO OBJ").grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="雁过留痕 @大水牛").grid(column=3, row=3, sticky=E)

feet_entry = scrolledtext.ScrolledText(mainframe, width=70, height=40, yscrollcommand=TRUE)
feet_entry.insert(INSERT, "输入JSON串")
feet_entry.grid(column=1, row=2, sticky=(W, E))
feet_entry.bind('<Key>', calculate)

meters_entry = scrolledtext.ScrolledText(mainframe, width=70, height=40, yscrollcommand=TRUE)
meters_entry.grid(column=3, row=2, sticky=(W, E))

ttk.Button(mainframe, text="转换", command=calculate).grid(column=2, row=2, sticky=(S, N))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()