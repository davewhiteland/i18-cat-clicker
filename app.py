# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_babel import Babel, gettext, ngettext
from flask_babel import gettext as _
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
babel = Babel(app)

MIDDAY = 12

def get_greeting():
  greeting = gettext("Good ")
  hour_now = datetime.now().time().hour
  if hour_now < MIDDAY: 
    greeting += gettext("morning")
  else:
    greeting += gettext("afternoon")
  return greeting


@app.route('/')
def index():
  
  greeting = gettext("Hello world.")
  
  return render_template('index.html', greeting=greeting)


@app.route('/greeting')
def greeting():
  
  return render_template('index.html', greeting=get_greeting() + ".")


@app.route('/name', methods = ['GET', 'POST'])
@app.route('/cats', methods = ['GET', 'POST'])
def name():
  
  if request.method == 'GET':
    return render_template('name.html',
      greeting    = gettext("Hello"),
      button_text = gettext("submit"),
      name_label  = gettext("Your name:"),
    )
  elif request.method == 'POST':
    name = request.form['name']
    qty_cats = len([s for s in request.form if s.startswith('cat')])

    greeting = get_greeting()
    if name:
      greeting += ", " + name
    greeting += "."
    
    plural_s = "s" 
    if qty_cats == 1:
      plural_s = ""
    else:
      plural_s = "s"

    cat_action = " ".join([gettext("You clicked on"), str(qty_cats), 
      gettext("cat") + plural_s + "."])

    return render_template('cats.html',
      greeting=greeting,
      name=name,
      cat_action=cat_action,
      button_text = gettext("meow"),
    )

@app.route('/about')
def about():
  return render_template('about.html')
