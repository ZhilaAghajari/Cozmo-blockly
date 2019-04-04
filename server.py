from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/click')
def click():
    print("something")
    return ""

@app.route('/pass_to_python', methods=['POST'])
def pass_to_python():
    print("something")
    return ""

if __name__ == '__main__':
    app.run(debug=True)
