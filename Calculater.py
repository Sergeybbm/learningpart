from tkinter import *
root = Tk()

e = Entry(width=60)
b = Button(text="Enter Name122")
l = Label(bg='black', fg='white', width=40)



def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)


b.bind('<Button-1>', strToSortlist)

e.pack()
b.pack()
l.pack()
root.mainloop()