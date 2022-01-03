from app import app
from flask import redirect, make_response, render_template, session
from db import db
from user import User
USER = User(db)
tiers = {
    2: "Master",
    10: "Owner"
}

@app.get("/")
def home():
    players = USER.high_tier_players()
    return render_template("/home.html", session=session, players=players, tiers=tiers)
    
@app.get("/login")
def login():
    return render_template("login.html")

@app.get("/register")
def register():
    return render_template("/register.html")

