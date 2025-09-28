import sqlite3

class Manager():
    def __init__(self,db):
      self.con=sqlite3.connect(db)
      self.cur=self.con.cursor()
      self.cur.execute('''create table if not exists manager 
                       (id integer primary key,name text,family text,address text,phone integer)''')
      self.con.commit()

    def insert(self,name,family,address,phone):
        self.cur.execute('insert into manager values (NULL,?,?,?,?)',(name,family,address,phone))
        self.con.commit()

    def remove(self,id):
       self.cur.execute('delete from manager where id = ?',(id,))
       self.con.commit()
    
    def update(self,id,name,family,address,phone):
       self.cur.execute('''update manager set 
                        name = ? ,family = ? ,address = ? , phone = ? where id = ?
                    ''',(name,family,address,phone,id))
       self.con.commit()
    

    def show_list(self):
      self.cur.execute('select *from manager ')
      return self.cur.fetchall()
      

    def search(self,name):
       self.cur.execute('''select * from manager
                        where id = ? or name = ? or family = ? or address = ? or phone = ? ''',
                        (name,name,name,name,name))
       records=self.cur.fetchall()
       return records
   



ma1=Manager('D:/p_database/cntact manager.db')    