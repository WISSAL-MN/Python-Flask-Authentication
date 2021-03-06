# Python-Flask-Authentication
Python Flask Authentication

# Usage :
Windows :

      python app.py

macOS/Linux :

      python3 app.py
      
      
# Flask-Bcrypt 1.0.1 :
Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application.
Due to the recent increased prevalence of powerful hardware, such as modern GPUs, hashes have become increasingly easy to crack. A proactive solution to this is to use a hash that was designed to be "de-optimized". Crypt is such a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are optimized for speed, crypt is intentionally structured to be slow.
For sensitive data that must be protected, such as passwords, bcrypt is an advisable choice.
# Installation :
      $ pip install flask-bcrypt
      
# Usage :
      from flask import Flask
      from flask_bcrypt import Bcrypt

      app = Flask(__name__)
      bcrypt = Bcrypt(app)
      
# Documentation :
>https://flask-bcrypt.readthedocs.io/

# Flask-WTF 1.0.1
Simple integration of Flask and WTForms
# Installation :
      pip install Flask-WTF
      
# LINKS :
Documentation: https://flask-wtf.readthedocs.io/


Changes: https://flask-wtf.readthedocs.io/changes/


PyPI Releases: https://pypi.org/project/Flask-WTF/


Source Code: https://github.com/wtforms/flask-wtf/


Issue Tracker: https://github.com/wtforms/flask-wtf/issues/


Chat: https://discord.gg/pallets

# Flask-SQLAlchemy 2.5.1 :
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

# Installation :
                $ pip install -U Flask-SQLAlchemy
                
# Usage:

      from flask import Flask
      from flask_sqlalchemy import SQLAlchemy

      app = Flask(__name__)
      app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
      db = SQLAlchemy(app)


      class User(db.Model):
          id = db.Column(db.Integer, primary_key=True)
          username = db.Column(db.String, unique=True, nullable=False)
          email = db.Column(db.String, unique=True, nullable=False)


      db.session.add(User(username="Flask", email="example@example.com"))
      db.session.commit()

      users = User.query.all()
                
 # LINKS :
 
 Documentation: https://flask-sqlalchemy.palletsprojects.com/
 
 
 Changes: https://flask-sqlalchemy.palletsprojects.com/changes/
 
 
 PyPI Releases: https://pypi.org/project/Flask-SQLAlchemy/
 
 
 Source Code: https://github.com/pallets/flask-sqlalchemy/
 
 
 Issue Tracker: https://github.com/pallets/flask-sqlalchemy/issues/
 
 
 Website: https://palletsprojects.com/
 
 
 Twitter: https://twitter.com/PalletsTeam
 
 
 Chat: https://discord.gg/pallets
      
# Flask-Login 0.6.1 :
Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users' sessions over extended periods of time.


# Installation :
                  $ pip install flask-login
                  
>https://pypi.org/project/Flask-Login/
>https://flask-login.readthedocs.io/en/latest/


# usage :
            from flask_login import LoginManager
            login_manager = LoginManager()

            login_manager.init_app(app)
