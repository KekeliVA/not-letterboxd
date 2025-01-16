from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)

app.run(host='0.0.0.0', port=5000)

@app.route("/", methods=["GET"])
def return_home():
  return jsonify({
    "message": "hello world"
  })

if __name__ == "__main__":
  app.run(debug=True)