from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health/')
def hello_world():
   return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)