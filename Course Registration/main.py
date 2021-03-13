from flask import *
app = Flask(__name__)
@app.route('/')
def register():
    return render_template('register.html')

def upload():
        return render_template("upform.html")
@app.route('/success', methods=['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        return render_template("data.html", result=result)

def success():
        if request.method == 'POST':
            f = request.files['file']
            f.save(f.filename)
            return render_template("upload.html", name=f.filename)

if __name__ == '__main__':
    app.run(debug=True)