from tkinter import *
import backend

win=Tk()

def get_selected_row(event):
        #print("get_selected_row() invoked")
        global data
        try:
            index=list.curselection()[0]
            data=list.get(index)
            e1.delete(0,END)
            e1.insert(END,data[1])
            e2.delete(0,END)
            e2.insert(END,data[3])
            e3.delete(0,END)
            e3.insert(END,data[2])
            e4.delete(0,END)
            e4.insert(END,data[4])
        except IndexError:
                pass
        
#Labels
l1=Label(win,text="Title").grid(row=0,column=0)
l2=Label(win,text="Year").grid(row=1,column=0)
l3=Label(win,text="Author").grid(row=0,column=2)
l4=Label(win,text="ISBN").grid(row=1,column=2)
#Values for each Entry
title_text=StringVar()
year_text=StringVar()
author_text=StringVar()
isbn_text=StringVar()
#Entries
e1=Entry(win,textvariable=title_text)
e1.grid(row=0,column=1)
e2=Entry(win,textvariable=year_text)
e2.grid(row=1,column=1)
e3=Entry(win,textvariable=author_text)
e3.grid(row=0,column=3)
e4=Entry(win,textvariable=isbn_text)
e4.grid(row=1,column=3)
#Listbox
list=Listbox(win,height=8,width=36)
list.grid(row=2,column=0,rowspan=6,columnspan=2)
#ScrollBar
sb=Scrollbar(win)
sb.grid(row=2,column=2,rowspan=7)
#Configuring Scrollbar with listbox
list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)
#List Binding 
list.bind('<<ListboxSelect>>',get_selected_row)
#Methods for buttons
def View_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)    
    list.delete(0,END)
    for row in backendbooks.view():
        list.insert(END,row)
def search_command():
    #clear_entry()
    list.delete(0,END)
    #list.insert(END,"Search in Entries")
    for row in backendbooks.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list.insert(END,row)
def add_command():
    s=''
    if s in [title_text.get(),author_text.get(),year_text.get(),isbn_text.get()]:
        list.delete(0,END)
        list.insert(END,"Please Enter All Details of Your book :)")
    else:
        backendbooks.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list.delete(0,END)
        list.insert(END,"Successfully Added..!")
def delete_command():
        backendbooks.delete(data[0])
        list.delete(0,END)
        list.insert(END,"Successfully Deleted from Store..!")
def update_command():
        #print(get_selected_row()[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        backendbooks.update(data[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list.delete(0,END)
        list.insert(END,"Successfully Updated..!")
def clear_command():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        list.delete(0,END)
#Buttons
b1=Button(win,text="View All",width=16,command=View_command).grid(row=2,column=3)
b2=Button(win,text="Search",width=16,command=search_command).grid(row=3,column=3)
b3=Button(win,text="Add Book",width=16,command=add_command).grid(row=4,column=3)
b4=Button(win,text="Update Selected",width=16,command=update_command).grid(row=5,column=3)
b5=Button(win,text="Delet Selected",width=16,command=delete_command).grid(row=6,column=3)
b6=Button(win,text="Clear All",width=16,command=clear_command).grid(row=7,column=3)



win.mainloop()
