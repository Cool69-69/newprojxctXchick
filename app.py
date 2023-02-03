from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TargetX25'


if __name__ == "__main__":
    app.run()
