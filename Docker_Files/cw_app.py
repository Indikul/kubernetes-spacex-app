#Importing required libraries
import os
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

#Configure db for the connection
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'cw_db'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #Fetch form data
        userDetails = request.form
        Name = userDetails['Name']
        Constellation = userDetails['Constellation']
        Decommission = userDetails['Decommission']
        Track = userDetails['Track']
        Control = userDetails['Control']
        Health = userDetails['Health']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cw(Name, Constellation, Decommission, Track, Control, Health) VALUES(%s, %s, %s, %s, %s, %s)",(Name, Constellation, Decommission, Track, Control, Health))
        mysql.connection.commit()
        cur.close()
        return redirect("/users") #Direct to the user page on the submit
    return render_template('index.html')

#Show data from the database
@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM cw")
    if resultValue > 0:
        userDetails = cur.fetchall()
    return render_template('user.html',userDetails=userDetails)
    if request.method == 'GET':
     return redirect ("/") #Direct to the home page on return

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

