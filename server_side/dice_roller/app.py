from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/roll", methods=["GET"])
def roll_dice():
    number = random.randint(1, 6)
    return jsonify({"number": number})

@app.route("/", methods=["GET"])
def home():
    return "Dice roller! Try <a href=\"/roll\">/roll</a>..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
