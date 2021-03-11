# i18n demo

## Tech

This is using [Flask-Babel](https://flask-babel.tkte.ch).


## Setup

Quick install dependencies like so:

    pip install -r requirements.txt

## How to run

Once it's setup, just run the Flask app (by default, Flask runs `app.py`):

    flask run

Then hit [localhost:5000](http://localhost:5000). 

Note `config.cfg` controls what languages you get back: to start with it's
`en`.

Kill flask on the command line with Crtl-C.

## How to translate

### Extract strings

    pybabel extract -F babel.cfg -o messages.pot .

This will use the mapping from the babel.cfg file and store the generated
template in `messages.pot`.


### Generate the translation file

Pick your language: here `de` for German:

    pybabel init -i messages.pot -d translations -l de

`-d translations` tells pybabel to store the translations in this folder. This
is where Flask-Babel will look for translations. 

### Translate the words

Now edit the `translations/de/LC_MESSAGES/messages.po` file as needed.

### Compile the translation

First time (new file):

    pybabel compile -d translations

Subsequently (updating translations):

    pybabel update -i messages.pot -d translations

That creates `messages.mo` in the `translations/de` directory.

Afterwards some strings might be marked as fuzzy (where it tried to figure out
if a translation matched a changed key). If you have fuzzy entries, make sure to
check them by hand and remove the fuzzy flag before compiling. _There won't be
any fuzzy strings the first time you run this._


### Run with translation

See if that worked: you should be able to switch to German by clicking on DE on
in the website (because that stores it in your session (cookie)).

Alternatively, if you want to force it, you can change the default language to German
in `get_locale` inside `app.py`.


### More detail when extracting

_Detail for later_:

If you are using the lazy_gettext() function you should tell pybabel that it
should also look for such function calls:

    pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
