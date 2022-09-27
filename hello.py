from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from markupsafe import escape
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name):
    if request.method == 'POST':
        print(request.json["users"][0]["email"])
        return f"sorry i cant create this resource yet, {escape(name)}!"
    else:
        return render_template('hello.html', name=name)


@app.route('/hello')
def hello1():
    print(url_for('show_post', post_id='123'))
    print("someone called hello")
    return f"Hello, Ak!"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'