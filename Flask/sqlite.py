from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3
conn = sqlite3.connect('database.db')
@app.route('/')
def new_student():
    return render_template('student1.html')
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin)VALUES(?, ?, ?, ?)",(nm,addr,city,pin) )
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result1.html", msg=msg)
            con.close()
if __name__ == '__main__':
 app.run(debug=True)
