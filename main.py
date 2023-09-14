from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from  db import Database

db=Database("employees.db")

root = Tk()
root.title("Employee management system")
root.geometry("1366x768+0+0")  # Corrected geometry specifier
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

# entries frame
entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee management system",font=("calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lalname=Label(entries_frame,text="Name",font=("calibri",16),bg="#535c68",fg="white")
lalname.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtname=Entry(entries_frame,textvariable=name,font=("calibri",16),width=30)
txtname.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lalage=Label(entries_frame,text="Age",font=("calibri",16),bg="#535c68",fg="white")
lalage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtage=Entry(entries_frame,textvariable=age,font=("calibri",16),width=30)
txtage.grid(row=1,column=3,padx=10,pady=10,sticky="w")

laldoj=Label(entries_frame,text="D.O.J",font=("calibri",16),bg="#535c68",fg="white")
laldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtdoj=Entry(entries_frame,textvariable=doj,font=("calibri",16),width=30)
txtdoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lalemail=Label(entries_frame,text="Email",font=("calibri",16),bg="#535c68",fg="white")
lalemail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtemail=Entry(entries_frame,textvariable=email,font=("calibri",16),width=30)
txtemail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lalgender=Label(entries_frame,text="Gender",font=("calibri",16),bg="#535c68",fg="white")
lalgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
combogender=ttk.Combobox(entries_frame,font=("calibri",16),width=28,textvariable=gender,state="readonly")
combogender['values']=("Male","Female")
combogender.grid(row=3,column=1,padx=10,pady=10,sticky="w")

lalcontact=Label(entries_frame,text="Contact",font=("calibri",16),bg="#535c68",fg="white")
lalcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtcontact=Entry(entries_frame,textvariable=contact,font=("calibri",16),width=30)
txtcontact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

laladdress=Label(entries_frame,text="Address",font=("calibri",16),bg="#535c68",fg="white")
laladdress.grid(row=4,column=0,padx=10,pady=10,sticky="w")

txtaddress=Text(entries_frame,width=85,height=5,font=("calibri",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,pady=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
    email.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0, END)
    txtaddress.insert(END,row[7])


def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add_employee():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("error input","please fill all the details")
        return
    db.insert(txtname.get(),txtage.get(),txtdoj.get(),txtemail.get(),combogender.get(),txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("success","Record Inserted")
    clearall()
    displayall()
def update_employee():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("error input","please fill all the details")
        return
    db.update(row[0],txtname.get(),txtage.get(),txtdoj.get(),txtemail.get(),combogender.get(),txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("success","Record Updated")
    clearall()
    displayall()

def delete_employee():
    db.remove(row[0])
    clearall()
    displayall()

def clearall():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0,END)

btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnadd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("calibri",16,"bold"),fg="white",bg="#16a085",bd=0).grid(row=0,column=0,padx=10)

btnedit=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=("calibri",16,"bold"),fg="white",bg="#2980b9",bd=0).grid(row=0,column=1,padx=10)

btndelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("calibri",16,"bold"),fg="white",bg="#c0392b",bd=0).grid(row=0,column=2,padx=10)

btnclear=Button(btn_frame,command=clearall,text="Clear Details",width=15,font=("calibri",16,"bold"),fg="white",bg="#f39c12",bd=0).grid(row=0,column=3,padx=10)

#table frame
tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=500,width=1400,height=400)

style=ttk.Style()
style.configure("mystyle.Treeview",font=('calibri',18),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('calibri',18))

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=20)
tv.heading("2",text="Name")
tv.heading("3",text="Age")
tv.column("3",width=20)
tv.heading("4",text="D.O.J")
tv.heading("5",text="Email")
tv.heading("6",text="Gender")
tv.column("6",width=20)
tv.heading("7",text="Contact")
tv.heading("8",text="Address")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)
displayall()
displayall()
root.mainloop()
