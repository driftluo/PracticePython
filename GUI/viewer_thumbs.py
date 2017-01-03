#! usr/bin/env python3
#--*--coding:utf8--*--

from tkinter import *
from PIL.ImageTk import PhotoImage
from PIL import Image
import os,sys,math

def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
	thumbdir = os.path.join(imgdir, subdir)
	if not os.path.exists(thumbdir):
		os.mkdir(thumbdir)

	thumbs = []
	for imgfile in os.listdir(imgdir):
		thumbpath = os.path.join(thumbdir, imgfile)
		if os.path.exists(thumbpath):
			thumbobj = Image.open(thumbpath)
			thumbs.append((imgfile, thumbobj))
		else:
			print('making', thumbpath)
			imgpath = os.path.join(imgdir, imgfile)
			try:
				imgobj = Image.open(imgpath)
				imgobj.thumbnail(size, Image.ANTIALIAS)
				imgobj.save(thumbpath)
				thumbs.append((imgfile, imgobj))
			except:
				print('Skipping:', imgpath)
	return thumbs

class ViewOne(Toplevel):
	def __init__(self, imgdir, imgfile):
		Toplevel.__init__(self)
		self.title(imgfile)
		imgpath = os.path.join(imgdir, imgfile)
		imgobj = PhotoImage(file=imgpath)
		Label(self, image=imgobj).pack()
		print(imgpath, imgobj.width(), imgobj.height())
		self.savephoto = imgobj

def viewer(imgdir, kind=Toplevel, cols=None):
	win = kind()
	win.title('Viewer:'+ imgdir)
	quit = Button(win, text='Quit', command=win.quit, bg='beige')
	quit.pack(fill=X, side=BOTTOM)
	thumbs = makeThumbs(imgdir)
	if not cols:
		cols = int(math.ceil(math.sqrt(len(thumbs))))

	savephotos = []
	while thumbs:
		thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
		row = Frame(win)
		row.pack(fill=BOTH)
		for (imgfile, imgobj) in thumbsrow:
			photo = PhotoImage(imgobj)
			link = Button(row, image=photo)
			handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
			link.config(command=handler)
			link.pack(side=LEFT, expand=YES)
			savephotos.append(photo)
	return win, savephotos

if __name__ == '__main__':
	imgdir = r'E:\壁纸\壁纸'
	main, save = viewer(imgdir, kind=Tk)
	main.mainloop()