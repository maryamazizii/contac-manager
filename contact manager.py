from tkinter import*
import manager_db
from tkinter import messagebox
win=Tk()
win.geometry('650x400')
win.configure(background="#F1EC8D")
win.title('contact manager')

#______________Function__________

ma1=manager_db.Manager('D:/p_database/cntact manager.db')

def clear_entry():
    entry_name.delete(0,END)
    entry_family.delete(0,END)
    entry_address.delete(0,END)
    entry_phone.delete(0,END)

def select_item(event):
    clear_entry()
    index=listbox.curselection()
    data=listbox.get(index)
    entry_name.insert(0,data[1])
    entry_family.insert(0,data[2])
    entry_address.insert(0,data[3])
    entry_phone.insert(0,data[4])


def insert_record():
    name=entry_name.get()
    family=entry_family.get()
    address=entry_address.get()
    phone=entry_phone.get()
    ma1.insert(name,family,address,phone)
    clear_entry()

def remove_record():
     result=messagebox.askquestion('WARNING','Dou you want it delete?')
     if result == 'yes':
        index=listbox.curselection()
        data=listbox.get(index)
        ma1.remove(data[0])
        show_list_record() 


def update_record():
    index=listbox.curselection()
    data=listbox.get(index)
    ma1.update(data[0],entry_name.get(),entry_family.get(),entry_address.get(),entry_phone.get())
    show_list_record()
    clear_entry()

def exit_ui():
    result=messagebox.askquestion('CLOSE','Dou you want exit?')
    if result=='yes':
        win.destroy()

def show_list_record():
   listbox.delete(0,END)
   records=ma1.show_list()
   for record in records:
       listbox.insert(END,record)


def search_record():
    listbox.delete(0,END)
    s_records=ma1.search(entry_search.get())
    for s_record in s_records:
        listbox.insert(END,s_record)
    entry_search.delete(0,END)
    if not s_records:
        listbox.configure(foreground='#8EC8E3',Text='the desired manager was not founda',font='tahoma 15')
        

    
#_____________Labale_____________

Label(win,text='Name',font='tahomma 12 ',background='#F1EC8D').place(x=90,y=25)
Label(win,text='address',font='tahomma 12 ',background='#F1EC8D').place(x=90,y=74)
Label(win,text='Family',font='tahomma 12 ',background='#F1EC8D').place(x=350,y=25)
Label(win,text='phone',font='tahomma 12 ',background='#F1EC8D').place(x=350,y=74)


#_____________Entry______________

entry_name = Entry(win,font='tahoma 10')
entry_name.place(x=157,y=26)

entry_address = Entry(win,font='tahoma 10')
entry_address.place(x=157,y=75)

entry_family = Entry(win,font='tahoma 10')
entry_family.place(x=411,y=26)

entry_phone = Entry(win,font='tahoma 10')
entry_phone.place(x=411,y=75)

entry_search = Entry(win,font='tahoma 10')
entry_search.place(x=170,y=178)


#____________Button_______________

btn_insert=Button(win,text='insert',font='tahoma 11',width=9,height=1,background='#8EC8E3',command=insert_record)
btn_insert.place(x=65,y=130)


btn_remove=Button(win,text='remove',font='tahoma 11',width=9,height=1,background="#8EC8E3",command=remove_record)
btn_remove.place(x=153,y=130)


btn_update=Button(win,text='update',font='tahoma 11',width=9,height=1,background='#8EC8E3',command=update_record)
btn_update.place(x=241,y=130)


btn_cleare=Button(win,text='cleare',font='tahoma 11',width=9,height=1,background='#8EC8E3',command=clear_entry)
btn_cleare.place(x=329,y=130)


btn_exit=Button(win,text='exit',font='tahoma 11',width=9,height=1,background='#8EC8E3',command=exit_ui)
btn_exit.place(x=417,y=130)

btn_show_list=Button(win,text='show list',font='tahoma 11',width=9,height=1,background='#8EC8E3',command=show_list_record)
btn_show_list.place(x=505,y=130)


btn_search=Button(win,text='search',font='tahoma 11',width=9,height=1,background='#8EC8E3',command=search_record)
btn_search.place(x=65,y=175)


#____________Listbox___________

listbox=Listbox(win,font='tahoma 11',width=57,height=8)
listbox.place(x=90,y=222)

sb=Scrollbar(win)
sb.place(x=532,y=224,height=153)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>',select_item)
win.mainloop()