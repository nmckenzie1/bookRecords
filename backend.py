import mysql.connector
def connect():
    con = mysql.connector.connect(
        user="root", 
        password = "Food414288!", 
        host="localhost", 
        database = "booksdb"
    )
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTO_INCREMENT, title text, author text, year integer, isbn integer)")
    con.commit()
    con.close()

def insert(title, author, year, isbn):
    con = mysql.connector.connect(
        user="root", 
        password = "Food414288!", 
        host="localhost", 
        database = "booksdb"
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO book (title,author,year,isbn) VALUES (%s,%s,%s,%s)",(title, author, year, isbn))
    con.commit()
    con.close()

def view():
    con = mysql.connector.connect(
        user="root", 
        password = "Food414288!", 
        host="localhost", 
        database = "booksdb"
    )
    cursor = con.cursor()
    cursor.execute("SELECT * FROM book")
    rows=cursor.fetchall()
    con.close()
    return rows

def search(title="",author="",year="",isbn=""):
    con = mysql.connector.connect(
        user="root", 
        password = "Food414288!", 
        host="localhost", 
        database = "booksdb"
    )
    cursor = con.cursor()
    cursor.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s", (title,author,year,isbn))
    rows=cursor.fetchall()
    con.close()
    return rows

def delete(idnum):
    con = mysql.connector.connect(
        user="root", 
        password = "Food414288!", 
        host="localhost", 
        database = "booksdb"
    )
    cursor = con.cursor()
    cursor.execute("DELETE FROM book WHERE id=%s", (idnum,))
    con.commit()
    con.close()

def update(title, author, year, isbn, idnum):
    con = mysql.connector.connect(
        user="root", 
        password = "Food414288!", 
        host="localhost", 
        database = "booksdb"
    )
    cursor = con.cursor()
    cursor.execute("UPDATE book SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", (title,author,year,isbn, idnum))
    con.commit()
    con.close()

connect()

