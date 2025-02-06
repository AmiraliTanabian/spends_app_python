import sqlite3
import datetime
import tabulate

conn = sqlite3.connect("../database.db")
cursor = conn.cursor()

def init():
    cursor.execute('''CREATE TABLE IF NOT EXISTS spends (
    name text, 
    category text, 
    pay text, 
    time text, 
    description text )
    ''')

def app_spend(name, category, pay, description = None):
    now = str(datetime.datetime.now())
    cursor.execute('''INSERT INTO spends VALUES (:name, :category, :pay, :time, :des)''',
                   {'name':name, 'category':category, 'pay':str(pay),'time':now, 'des':description})
    conn.commit()

def show(category=None):
    if category != None :
        cursor.execute('''SELECT * FROM spends WHERE category = :category''',
                       {'category':category})
    else :
        cursor.execute('''SELECT * FROM spends''')
    return cursor.fetchall()

def update(old_name, old_category, new_name, new_cat, new_price, new_time, new_des):
    cursor.execute('''UPDATE spends SET name = :n, category=:c, pay=:p, time=:t, description=:d WHERE name = :on AND category = :oc''', 
                   {'n':new_name, 'c':new_cat, 'p':new_price, 't':new_time, 'd':new_des, 'on':old_name, 'oc':old_category})
    conn.commit()
def delete(name, category):
    cursor.execute('''DELETE FROM spends WHERE name = :name AND category = :cat''', {'name':name.strip(), 'cat':category.strip()})
    conn.commit()


init()

