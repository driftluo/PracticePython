#! usr/bin/env python3
#--*--coding:utf8--*--

import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askfloat

demos = {
	'Open': askopenfilename,
	'Color': askcolor,
	'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
	'Error': lambda: showerror('Error!', "He's dead, Jim"),
	'Input': lambda: askfloat('Entry', 'Enter credit card number')
}

class Quitter(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		widget = Button(self, text='Quit', command=self.quit)
		widget.pack(side=LEFT, expand=YES, fill=BOTH)

	def quit(self):
		ans = askokcancel('Verify exit', 'Really quit?')
		if ans: Frame.quit(self)

class Demo(Frame):
	def __init__(self, parent=None, **options):
		Frame.__init__(self, parent, **options)
		self.pack()
		Label(self, text='Basic demos').pack()
		for (key, value) in demos.items():
			func = (lambda key=key: self.printit(key))
			Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
		Quitter(self).pack(side=TOP, fill=BOTH)

	def printit(self, name):
		print(name, 'returns =>', demos[name]())

Demo().mainloop()