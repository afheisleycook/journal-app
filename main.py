import tkinter as tk
import sqlite3
def create_db():
    conn = sqlite3.connect("journal.db")


create_db()

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lbltitle = tk.Label(text="title", relief="flat")
        self.lbltitle.grid(column=1,row=1)
        self.txtTitle = tk.Entry()
        self.txtTitle.grid(column=2,row=1)
        self.lbldescription = tk.Label(text="description", relief="flat")
        self.lbldescription.grid(column=1, row=2)
        self.txtdescri = tk.Text()
        self.txtdescri.grid(column=2, row=2)
        self.btnadd = tk.Button(self,command=self.insert,text="insert")
        self.btnadd.grid(row=4,column=3,)
    def insert(self):
        conn = sqlite3.connect("journal.db")
        conn.execute(f"insert into log values(0,{self.txtTitle.get()},{self.txtdescri.get(1.0, 'end')}')")





mainwindow = MainWindow()
mainwindow.mainloop()

