# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_babel import Babel, gettext, ngettext
from flask_babel import gettext as _
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
babel = Babel(app)

MIDDAY = 12

def get_greeting(name=None):
  hour_now = datetime.now().time().hour
  if hour_now < MIDDAY: 
    if name is None:
      greeting = gettext("Good morning.")
    else:
      greeting = gettext("Good morning, %(name)s. ", name=name)
  else:
    if name is None:
      greeting = gettext("Good afternoon.")
    else:
      greeting = gettext("Good afternoon, %(name)s. ", name=name)
  return greeting


@app.route('/')
def index():
  greeting = gettext("Hello world.")
  return render_template('index.html', greeting=greeting)


@app.route('/greeting')
def greeting():
  return render_template('index.html', greeting=get_greeting())


@app.route('/name', methods = ['GET', 'POST'])
@app.route('/cats', methods = ['GET', 'POST'])
def name():
  if request.method == 'GET':
    return render_template('name.html',
      greeting    = gettext("Hello"),
      # NOTE submit appears on a button sumitting a form that collects user's name
      button_text = gettext("submit"),
      name_label  = gettext("Your name:"),
    )
  elif request.method == 'POST':
    name = request.form['name']
    qty_cats = len([s for s in request.form if s.startswith('cat')])
    greeting = get_greeting(name)
    # NOTE: the user has previously clicked on a number of pictures of cats
    cat_action = ngettext(
      "You clicked on %(num)s cat.",
      "You clicked on %(num)s cats.", qty_cats)
    return render_template('cats.html',
      greeting=greeting,
      name=name,
      cat_action=cat_action,
      # NOTE this appears on the button the user must click to submit choice of cats
      button_text = gettext("meow"),
    )


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == "__main__":
    app.run()