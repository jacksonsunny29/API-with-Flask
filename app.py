from flask import flask
app=Flask(__name__)

@app.route('/')
def api():
    return "<h1>Hello</h1>"

if __name__ == "__main__":
    app.run(debug=True,threaded=True)    