#! usr/bin/env python3
#--*--coding:utf8--*--

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
		Label(self, text='Radio demos').pack(side=TOP)
		self.var = StringVar()
		for key in demos:
			Radiobutton(self, text=key, command=self.onPress, variable=self.var, value=key).pack(anchor=NW)
		self.var.set(key)
		Button(self, text='State', command=self.report).pack(fill=X)
		Quitter(self).pack(fill=X)

	def onPress(self):
		pick = self.var.get()
		print('you pressed', pick)
		print('result:', demos[pick]())

	def report(self):
		print(self.var.get())

Demo().mainloop()