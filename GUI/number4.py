#! usr/bin/env python3
#--*--coding:utf8--*--

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askfloat


class Quitter(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		widget = Button(self, text='Quit', command=self.quit)
		widget.pack(side=LEFT, expand=YES, fill=BOTH)

	def quit(self):
		ans = askokcancel('Verify exit', 'Really quit?')
		if ans: Frame.quit(self)

demos = {
	'Open': askopenfilename,
	'Color': askcolor,
	'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
	'Error': lambda: showerror('Error!', "He's dead, Jim"),
	'Input': lambda: askfloat('Entry', 'Enter credit card number')
}

class Demo(Frame):
	def __init__(self, parent=None, **options):
		Frame.__init__(self, parent, **options)
		self.pack()
		self.tools()
		Label(self, text='Check demos').pack()
		self.vars = []
		for key in demos:
			var = IntVar()
			Checkbutton(self,
						text=key,
						variable=var,
						command=demos[key]).pack(side=LEFT)
			self.vars.append(var)

	def report(self):
		for var in self.vars:
			print(var.get(), end=' ')
		print()

	def tools(self):
		frm = Frame(self)
		frm.pack(side=RIGHT)
		Button(frm, text='State', command=self.report).pack(fill=X)
		Quitter(frm).pack(fill=X)

Demo().mainloop()