from flask import *
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('post.html');

@app.route('/login',methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "sai" and passwrd == "sai":
        return "Welcome %s" %uname
if __name__=="__main__":
    app.run(debug=True)