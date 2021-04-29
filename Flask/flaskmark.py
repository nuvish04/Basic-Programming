from flask import Flask, render_template
app = Flask(__name__,template_folder='templates')
@app.route('/mark/<int:score>')
def hello_name(score):
 return render_template('mark.html', marks = score)
if __name__ == '__main__':
 app.run(debug = True)