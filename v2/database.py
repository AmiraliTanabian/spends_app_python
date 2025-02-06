import sqlite3
import datetime
import tabulate

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def createTable():
    conn = sqlite3.connect("database.db")


def init():
    cursor.execute('''CREATE TABLE IF NOT EXISTS spends (
    name text, 
    category text, 
    pay text, 
    time text, 
    description text )
    ''')

def app_spend(name, category, pay, description = None):
    now = datetime.datetime.now()
    now_year = now.year - 2000
    now_month = now.month
    now_day = now.day

    now = str(datetime.datetime.now().strftime(f'{now_year}/{now_month}/{now_day} | %H:%M'))
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

# def FilterdShow(name, date, category):
#     if date == None and category == None :
#         cursor.execute('''SELECT * FROM spends WHERE name=:name''', {'name':name})
#         return cursor.fetchall()

init()
