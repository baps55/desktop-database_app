from tkinter import *
import backend

def get_selected_row(event):    #a special arg event is passed to this function as it binds to an event
    try:
        global selected_tuple   #declaring global variable for use in outside the function
        index=list1.curselection()[0]  #to capture the index of the selected row to delete
        selected_tuple=list1.get(index) #returns a tuple of the selected row from list box
        #return(selected_tuple)
        #for the Update button, doing this will populate the text boxes with respective values of the selected row from list-box
        e1.delete(0,END)            #delete everything in the book Title field
        e1.insert(END,selected_tuple[1])    #insert new value for the book Title field
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
        #the try/except block was used to bypass the "IndexError" caused due to clicking on the list-box when empty

def view_cmd():
    list1.delete(0,END) # to delete the output of the previous View All cmd, else the same output is repeated
    for row in backend.view(): #iterating through the rows returned from the view() in backend.py
        list1.insert(END,row) #the END keyword ensures each row is positioned at the end of the list box

def search_cmd():
    list1.delete(0,END) # to delete the output of the previous View All cmd, else the same output is repeated
    for row in backend.search(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()): # the get() helps to output a simple string
        list1.insert(END,row)                                                       # object from a StringVar type

def add_cmd():
    backend.insert(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
    list1.delete(0,END)
    list1.insert(END,(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())) # to see the newly added entry

def del_cmd():
    backend.delete(selected_tuple[0])   #using get_selected_row()[0] was throwing an error saying arg 'event' was missing
                                        #so we used selected_tuple instead which directly passes the id of the row to be deleted

def update_cmd():
    backend.update(selected_tuple[0],e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()) #to update the DB with values in the text boxes


window=Tk()
window.wm_title="Bookstore"

l1=Label(window,text="Title")                   #creating labels for the buttons
l1.grid(row=0,column=0)

e1_val=StringVar()                              #mapping buttons to variable for storing data
e1=Entry(window,textvariable=e1_val,width=20)
e1.grid(row=0,column=1)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

e2_val=StringVar()
e2=Entry(window,textvariable=e2_val,width=20)
e2.grid(row=0,column=3)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

e3_val=StringVar()
e3=Entry(window,textvariable=e3_val,width=20)
e3.grid(row=1,column=1)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

e4_val=StringVar()
e4=Entry(window,textvariable=e4_val,width=20)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=50)             #creating a list box to display result of a button action
list1.grid(row=3,column=0,rowspan=5,columnspan=2)

sb1=Scrollbar(window)                               #creating scroll-bar for list box
sb1.grid(row=3,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",get_selected_row)    #the bind() can be used to bind a function to a widget event
                                                    #e.g. selecting a row from list box for deletion
                                                    #the bind() takes 2 args: event type and the function to bind

b1=Button(window,text="View all",width=12,command=view_cmd)
b1.grid(row=3,column=3)

b2=Button(window,text="Search entry",width=12,command=search_cmd)
b2.grid(row=4,column=3)

b3=Button(window,text="Add entry",width=12,command=add_cmd)
b3.grid(row=5,column=3)

b4=Button(window,text="Update",width=12,command=update_cmd)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete",width=12,command=del_cmd)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)  #to close the window
b6.grid(row=8,column=3)

window.mainloop()
