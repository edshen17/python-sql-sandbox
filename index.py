import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=path where you stored the Access file\file name.accdb;')
cursor = conn.cursor()
cursor.execute('select * from table name')
   
for row in cursor.fetchall():
    print (row)

import mysql.connector

cnx = mysql.connector.connect(user='root', password='bluewater2',
                              host='localhost',
                              database='python_sandbox')
cursor = cnx.cursor()

def teacher_or_student(role):
    if role == 'T':
        query = ('SELECT * FROM teachers')
    elif role == 'S':
        query = ('SELECT * FROM students')
    return query
        

while True:
    role = input('Are you a teacher (T) or student (S)?')
    query = teacher_or_student(role)
    cursor.execute(query)
    inputUsername = input('Username:')
    inputPassword = input('Password:')

    for (tid, username, password) in cursor:
        if username == inputUsername and password == inputPassword:
            success = 'Login Successful. \n Welcome, {}, to SYSTEM. \n Name List - (N) \n New Entry - (E) \n Modify Entry - (M) \n Logout - (L)'.format(username)
            print(success)
            continue
    #     continue
    # else
    #     print('Please enter a valid input!')
    # break

