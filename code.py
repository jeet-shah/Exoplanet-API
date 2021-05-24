from flask import Flask,jsonify,request
from data import data
app = Flask(__name__)
@app.route("/planet")
def planet():
    name = request.args.get("name")
    pl_data = next(i for i in data if i["name"] == name)
    return jsonify({
        "data":pl_data,
        "message":"Success"
    }),200
if __name__ == "__main__":
    app.run()