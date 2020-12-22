from flask import Flask
from flask import Flask,render_template,url_for,request,session,logging,redirect,flash
import pyodbc 

app = Flask(__name__)
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1K6HH4D\SQLEXPRESS;'
                      'Database=DBT_Lab_7;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
print("Connection Established")

cursor.execute('SELECT * FROM DBT_Lab_7.dbo.Students')
#for row in cursor:
 #   print(row)
print("Done")

#def student(Stud):

@app.route('/')
def auth():
    return render_template('auth.html')

@app.route('/home')
def home():
    return render_template('homenew.html')

@app.route('/home/chart')
def chart():
    return render_template('chart.html')

if __name__ == "__main__":
    app.run()


'''
#THIS IS TO IMPORT FLASK METHODS

from flask import Flask, render_template

#THIS IS TO ESTABLISHING THE CONNECTION WITH DB
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1K6HH4D\SQLEXPRESS;'
                      'Database=DBT_Lab_7;'
                      'Trusted_Connection=yes;')

#THIS IS TO SET THE FLASK PROPERTY
# app = Flask(_name_)

#THIS IS TO DESCRIBE THE HOME PAGE(INDEX PAGE)
@app.route('/')
#THE index page specification
def index():
    return render_template('index.html')

@app.route('/list_user')
def list_view():
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM DBT_Lab_7.dbo.Students")
    response = mycursor.fetchall()
    return render_template('demo_list.html',response=response)
    
if __name__ == "__main__":
    app.run()
'''