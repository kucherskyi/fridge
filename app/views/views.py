from flask import render_template

from app.app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           user='Artem',
                           title='Home')
