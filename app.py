from flask import Flask
from os import getenv
app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
print("jutut:")
print(getenv("SECRET_KEY"))
print(app.config)
import routes
import authentication