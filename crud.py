import mysql.connector as conector
class sql:
    def __init__(self):
        self.con = conector.connect(host='localhost', port='3306', user='root', password='rahul', database='college') 
        query = 'CREATE table if not exists student(studentId INT primary key, userName varchar(50), phone int(11))'
        self.cur = self.con.cursor()
        self.cur.execute(query)
        print('created')
        
    def execute(self, query):
        print(query)
        self.cur.execute(query)
        self.con.commit()
        
    def insert(self,userId, userName , phone):
        query=f'INSERT into student VALUES { ( userId, userName, int(phone)) };'
        self.execute(query)
        print("Created new user")
        
    def fetch(self, studentId):
        query=f"Select * from student where studentId={studentId}"
        self.cur.execute(query)
        for row in self.cur:
            return row[0] ,row[1], row[2]
            
    def delete(self, userId):
        query = f"DELETE FROM student WHERE studentId = {userId};"
        self.execute(query)
        print('Deleted')
        
    def update(self, studentId, userName, phone):
        query =  f"Update student set userName='{userName}', phone='{phone}' where studentId = {studentId}"
        self.execute(query)
        print('Updated')
    
from  tkinter import *
from tkinter import messagebox as mb 
import tkinter.font as font
sql=sql()


def clear():
    id.delete(0,END)
    name.delete(0,END)
    phone.delete(0,END)
def error():
    mb.showerror('ERROR',"Please valid details")
def check():
    if(id.get=="" or name.get()=='' or phone.get()==''):
        error()
        return False
    else:
        return True
def insert():
    if(check()):
        sql.insert(id.get(), name.get(), phone.get())
        mb.showinfo(title='Done', message="Added successfully")
        clear()
        
def update():
    if(check()):
        sql.update(id.get(), name.get(), phone.get() )
        mb.showinfo(title='Done', message="Updated successfully")
        clear()

def delete():
    if(id.get()!=""):
        sql.delete(id.get())
        mb.showinfo(title='Done', message="Deleted successfully")
        clear()
    else:
        error()
def search():
    if(id.get()!=""):
        row=sql.fetch(id.get())
        name.insert(0,row[1])
        phone.insert(0,row[2])
    else:
        error()

window = Tk()
# window.maxsize(600, 250)
window.minsize(600,300)
window.title("Data Collector")
main_frame = Frame(window, )
main_frame.pack( fill= BOTH ,side=  TOP)

frame = Frame(main_frame)
frame.pack( fill= BOTH ,side=  TOP)

frame2 = Frame(main_frame)
frame2.pack( fill= BOTH,side=  TOP)


frame3 = Frame(main_frame)
frame3.pack( fill= BOTH,side=  TOP)

frame4 = Frame(main_frame)
frame4.pack( fill= BOTH,side=  BOTTOM)

label =  Label(frame,text = "Enter StudentId :",font=('calibre',15,'normal') )
label.pack(side = LEFT, expand = True,padx=5, pady=15)

id =  Entry(frame,font=('calibre',20,'normal') )
id.pack(side = LEFT, expand = True ,padx=5, pady=15)

label2 =  Label(frame2, text = "Enter Student Name :" ,font=('calibre',15,'normal'))
label2.pack(side = LEFT, expand = True,padx=5, pady=15,fill = BOTH)

name =   Entry(frame2,font=('calibre',20,'normal') )
name.pack(side = LEFT, expand = True, padx=5, pady=15)

label3 =  Label(frame3, text = "Phone number Data :" ,font=('calibre',15,'normal') )
label3.pack( side = LEFT, expand = True, padx=5, pady=15,fill = BOTH )

phone =  Entry(frame3,font=('calibre', 20, 'normal') )
phone.pack(side = LEFT, expand = True, padx=5, pady=15)

b1 =  Button(frame4, text = "ADD", bg='#293d3d', fg = "#66d9ff", font=('calibre',15,'normal'), command=insert)
b1.pack(side = LEFT, expand = True,padx=5, pady=15,fill = BOTH)

b2 =  Button(frame4, text = "UPDATE", bg='#293d3d', font=('calibre',15,'normal'), fg = "#66d9ff" ,command=update)
b2.pack( side = LEFT, expand = True,padx=5, pady=15 ,fill = BOTH)

b3 =  Button(frame4, text = "DELETE", bg='#293d3d', font=('calibre',15,'normal') , fg = "#66d9ff" ,command=delete)
b3.pack( side = LEFT, expand = True,padx=5, pady=15,fill = BOTH )

b4 =  Button(frame4, text = "SEARCH", bg='#293d3d', font=('calibre',15,'normal') , fg = "#66d9ff" ,command=search)
b4.pack( side = LEFT, expand = True,padx=5, pady=15,fill = BOTH )

window.mainloop()

