from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

JSON_FILE = os.path.join("data", "students.json")

@app.route("/students", methods=["GET"])
def get_students():
    try:
        with open(JSON_FILE, "r") as f:
            students = json.load(f)
        return jsonify(students), 200
    except FileNotFoundError:
        return jsonify({"error": "students.json no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

