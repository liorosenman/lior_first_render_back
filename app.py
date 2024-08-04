from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"msg":"Peace to the world"}

if __name__ == '__main__':
    app.run(debug=True)

