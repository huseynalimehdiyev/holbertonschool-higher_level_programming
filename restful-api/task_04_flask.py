from flask import Flask, jsonify, request

app = Flask(__name__)

# -------------------------
# In-memory storage
# -------------------------
users = {}


# -------------------------
# ROOT
# -------------------------
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


# -------------------------
# STATUS
# -------------------------
@app.route("/status", methods=["GET"])
def status():
    return "OK"


# -------------------------
# DATA (list usernames)
# -------------------------
@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys()))


# -------------------------
# GET USER BY USERNAME
# -------------------------
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


# -------------------------
# ADD USER (POST)
# -------------------------
@app.route("/add_user", methods=["POST"])
def add_user():

    # validate JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # check username
    if "username" not in data or not data["username"]:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # duplicate check
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # create user object
    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user

    return jsonify({
        "message": "User added",
        "user": user
    }), 201


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=False)
