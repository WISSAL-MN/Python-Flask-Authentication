# Python-Flask-Authentication
Python Flask Authentication

# Usage
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

      
      
