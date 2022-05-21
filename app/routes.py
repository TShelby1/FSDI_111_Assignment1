from flask import Flask # from flask module import the flask class

app = Flask(__name__) #

@app.get("/")
def index():
    me = {
        "first_name": "Albert",
        "last_name": "Lara",
        "hobbies": "DIY, fishing, eating food"
    }
    return me