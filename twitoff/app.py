""" Create and configure an instance of the Flask Application """
from flask import Flask, render_template
from .models import DB, User

def create_app():
    """ Main application  function for twitoff """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    @app.route('/')
    def root():
        # Drops everything from DB
        DB.drop_all()
        # Creates DB
        DB.create_all()
        insert_example_users()
        return render_template('base.html', title="Home")
    # @ app.route('/hola')
    # def hola():
    #     return "hola, Twitoff"
    # @ app.route('/salut')
    # def salut():
    #     return "salut, Twitoff"
    # return app
def insert_example_users():
    """ Insert hypothetical users """
    nick = User(id=1, name="nick")
    elon = User(id=2, name="elonmusk")
    DB.session.add(nick)
    DB.session.add(elon)
    DB.session.commit()