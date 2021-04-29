from flask import Flask
app = Flask(__name__)
@app.route('/<name>')
def hello_name(name):
    return 'Hello %s!' % name
@app.route('/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID
@app.route('/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo
if __name__ == '__main__':
    app.run(debug=True)
