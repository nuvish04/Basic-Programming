from flask import Flask, render_template
app = Flask(__name__)
import sqlite3
@app.route('/')
def list():
    con = sqlite3.connect('database.db')
    con.row_factory =sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template("list.html", rows=rows)
if __name__ == '__main__':
 app.run(debug=True)
