from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/download', methods=['POST'])
def download():
    # http://stackoverflow.com/a/20341272/1713757
    git_url = request.values.get("git_url")
    # git_url = request.form["git_url"]
    print(git_url)
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)