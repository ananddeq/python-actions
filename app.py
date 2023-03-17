from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return "First page of REST API"

@app.get("/api")
def get_room():
    return "Inside the room"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000")
