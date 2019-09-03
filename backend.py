import sqlite3
def connect():
    con=sqlite3.connect("booksstore.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Books(id INTEGER PRIMARY KEY,Title TEXT,AuthorName TEXT,Year INTEGER,ISBN INTEGER)")
    con.commit()
    con.close()
def insert(title,author,year,isbn):
    con=sqlite3.connect("booksstore.db")
    cur=con.cursor()
    cur.execute("INSERT INTO Books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()
def view():
    con=sqlite3.connect("booksstore.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Books")
    rows=cur.fetchall()
    con.close()
    return rows
def search(title=None,author=None,year=None,isbn=None):
    con=sqlite3.connect("booksstore.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Books WHERE Title=? OR AuthorName=?  OR Year=? OR ISBN=?",(title,author,year,isbn))
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows
def delete(id):
    con=sqlite3.connect("booksstore.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Books WHERE id=?",(id,))
    con.commit()
    con.close()
def update(id,title,author,year,isbn):
    con=sqlite3.connect("booksstore.db")
    cur=con.cursor()
    #print(title,author,year,isbn)
    cur.execute("UPDATE Books SET Title=?,AuthorName=?,Year=?,ISBN=? WHERE id=?",(title,author,year,isbn,id))
    con.commit()
    con.close()
connect()
