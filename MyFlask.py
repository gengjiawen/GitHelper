import ntpath
import os
import tempfile

from flask import Flask
from flask import render_template
from flask import request
from flask import send_file

import file_util
import py7z_util

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/download', methods=['POST'])
def download():
    # http://stackoverflow.com/a/20341272/1713757
    git_url = request.values.get("git_url")
    print(git_url)
    # git_url = request.form["git_url"]

    # download code
    folder = tempfile.mkdtemp()
    git_clone_cmd = r"git clone {}".format(git_url)
    os.chdir(folder)
    os.system(git_clone_cmd)

    # compress code
    code = os.path.join(folder, file_util.get_immdiate_dir(folder)[0]) + ".7z"
    py7z_util.compress(code, folder + "/*")
    response = send_file(code, mimetype='application/x-7z-compressed', as_attachment=True,
                         attachment_filename=ntpath.basename(code))
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
