#! usr/bin/env python3
#--*--coding:utf8--*--

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askfloat

root = Tk()
scl = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(expand=YES, fill=Y)

def report():
	print(scl.get())

Button(root, text='state', command=report).pack(side=RIGHT)
root.mainloop()