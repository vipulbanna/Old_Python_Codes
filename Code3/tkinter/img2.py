from tkinter import *
root = Tk()
img = PhotoImage(file="./small.gif")
#w1 = Label(root,image=img).pack(side="right")
exp="""Hey this to inform you that at 
present the python3 only support
gif,PPM/PGM image files in 
tkinter module. In future we will
see by interfacing we can use all
type of images """
w = Label(root,justify=LEFT,compound=LEFT,padx=10,text=exp,bg="light blue",fg="dark green",image=img).pack(side='right')
root.mainloop()
