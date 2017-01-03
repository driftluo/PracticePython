#! usr/bin/env python3
#--*--coding:utf8--*--

from tkinter import *

class Checkbar(Frame):
	def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
		Frame.__init__(self, parent)
		self.vars = []
		for pick in picks:
			var = IntVar()
			chk = Checkbutton(self, text=pick, variable=var)
			chk.pack(side=side, anchor=anchor, expand=YES)
			self.vars.append(var)

	def state(self):
		return [var.get() for var in self.vars]

class Radiobar(Frame):
	def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
		Frame.__init__(self, parent)
		self.var = StringVar()
		self.var.set(picks[0])
		for pick in picks:
			rad = Radiobutton(self, text=pick, value=pick, variable=self.var)
			rad.pack(side=side, anchor=anchor, expand=YES)

	def state(self):
		return self.var.get()

if __name__ == '__main__':
	root = Tk()
	lng = Checkbar(root, ['Python', 'C#', 'Java', 'C++'])
	gui = Radiobar(root, ['win', 'x11', 'mac'], side=TOP, anchor=NW)
	tgl = Checkbar(root, ['All'])

	gui.pack(side=LEFT, fill=Y)
	lng.pack(side=TOP, fill=X)
	tgl.pack(side=LEFT)
	lng.config(relief=GROOVE, bd=2)
	gui.config(relief=RIDGE)

	def allstates():
		print(gui.state(), lng.state(), tgl.state())

	from tkinter.messagebox import *

	class Quitter(Frame):
		def __init__(self, parent=None):
			Frame.__init__(self, parent)
			self.pack()
			widget = Button(self, text='Quit', command=self.quit)
			widget.pack(side=LEFT, expand=YES, fill=BOTH)

		def quit(self):
			ans = askokcancel('Verify exit', 'Really quit?')
			if ans: Frame.quit(self)

	Quitter(root).pack(side=RIGHT)
	Button(root, text='Peek', command=allstates).pack(side=RIGHT)
	root.mainloop()