import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Useless API</h1><p>I just wasted resources.</p>"

app.run(host='0.0.0.0',port=8080)
