from app import app
from flask import redirect, make_response, render_template, session
from db import db
from user import User
import json
USER = User(db)
tiers = {
    6: "Owner",
    5: "God",
    4: "Elite",
    3: "Pro"
}

@app.get("/")
def home():
    players = USER.all()
    return render_template("/home.html", session=session, players=players, tiers=tiers)
    
@app.get("/login")
def login():
    return render_template("login.html")

@app.get("/register")
def register():
    return render_template("/register.html")

@app.get("/name-wall")
def name_wall():
    with open('players.json') as json_file:
            json_data = json.load(json_file)
    return render_template("/name-wall.html", players=json_data, tiers=tiers)