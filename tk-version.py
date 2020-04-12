from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Download File")
root.geometry("300x160")
root.iconbitmap("Linux.ico")
messagebox.showinfo("hello tkinter")
#label=Label(root,text="tkinter").pack()
label=Label(root,text="hello tkinter")
label.pack()
label["text"]="again"
label["text"]="%d" % 55

root.mainloop()
#print(tkinter.TkVersion)
