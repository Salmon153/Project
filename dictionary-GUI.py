from tkinter import*
import app
win=Tk()
def list_of_meanings(meaning):
    for i in range(len(meaning)):
        t.insert(END,str(i+1)+" "+meaning[i]+"\n")
def search_command():
    global meaning
    t.delete('1.0',END)
    meaning=app.translate(word.get())
    if type(meaning) == list:
        list_of_meanings(meaning)
    else:
        t.insert(END,"Word "+word.get()+" doesn't exist \nInsted we have \n"+meaning+" = ")
        wor=app.translate(meaning)
        list_of_meanings(wor)
        
l1=Label(win,text="Enter Word").grid(row=0,column=0)
word=StringVar()
e=Entry(win,textvariable=word)
e.grid(row=0,column=1)
l2=Label(win,text="Meaning:").grid(row=2,column=0)
t=Text(win,height=10,width=20)
t.grid(row=3,columnspan=2)
sb=Scrollbar(win)
sb.grid(row=3,column=2,rowspan=7)
t.configure(yscrollcommand=sb.set)
sb.configure(command=t.yview)
b=Button(win,text="Search",command=search_command).grid(row=1,column=0)
win.mainloop()
