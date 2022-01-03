from app import app
from flask import request, render_template, redirect, session
from user import User
import uuid
from db import db
import bcrypt
USER = User(db)
import os,binascii

@app.post("/register")
def handle_register():
    if request.form["password"]!=request.form["password_confirmation"]:
        return render_template("/register.html", error_message="Passwords do not match.")
    try:
        USER.new(request.form)
        USER.commit()
    except Exception:
        return render_template("/register.html", error_message="Username already taken. If this name is owned by you, contact Super on discord.")
    return redirect("/login")

@app.post("/login")
def handle_login():
    try:
        data = USER.authenticate(request.form)
        session["username"]=data["username"]
        session["tier"]=data["tier"]
        session["CSRF_token"]=binascii.b2a_hex(os.urandom(15))
    except Exception:
        return render_template("/login.html", error_message="Incorrect username or password.")
    return redirect("/")

    


