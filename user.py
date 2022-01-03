from db import db
import bcrypt
import json


class User:
    def __init__(self, db: db):
        self.db=db

    def high_tier_players(self):
        players = self.db.session.execute("select username, tier from users where tier>0")
        return players
        
    def all (self):
        players = self.db.session.execute("select username, tier from users").fetchall()
        return players

    def new(self, data):
        with open('players.json') as json_file:
            json_data = json.load(json_file)

        password = data["password"].encode()
        tier=0
        if data["username"].capitalize() in json_data:
            tier=2

        hash = bcrypt.hashpw(password, bcrypt.gensalt())
        print("jutut:")
        self.db.session.execute("insert into users (username, password, tier) values (:name, :password, :tier)", 
        {
            "name": data["username"],
            "password": hash.decode(),
            "tier": tier
        })

    def get_user_data(self, username):
        data = db.session.execute("select * from users where username=:username", {"username": username}).fetchall()
        return data[0]

    def authenticate(self, data):
        user_data = self.get_user_data(data["username"])
        password = user_data[2]
        if bcrypt.checkpw(data["password"].encode(), password.encode()):
            return user_data
        raise ValueError

    def commit(self):
        self.db.session.commit()
    
