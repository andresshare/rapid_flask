from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/params")
def params():
    param =  request.args.get('params1', ' No contiene este parametro')
    return "El parametro es: {}".format(param)

if __name__ == "__main__":
    app.run(debug = True,port='8000')    