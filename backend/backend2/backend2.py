from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/api/data", methods=["GET"])
def get_data():
  return jsonify({"message": "Hello from backend 2"})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000) # for kubernetes use
  # app.run(host="0.0.0.0", port=5002) # for local use
