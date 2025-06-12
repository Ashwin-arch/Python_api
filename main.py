from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory user store
users = {
    "1": {"name": "John Doe", "email": "john.doe@example.com"}
}

# GET: Retrieve user info
@app.route("/get-user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        extra = request.args.get("extra")
        if extra:
            user["extra"] = extra
        return jsonify({"user_id": user_id, **user})
    return jsonify({"error": "User not found"}), 404

# POST: Create new user
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = {
        "name": data["name"],
        "email": data["email"]
    }
    return jsonify({"message": "User created", "user_id": user_id}), 201

# PUT: Update existing user
@app.route("/update-user/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update({
        "name": data.get("name", users[user_id]["name"]),
        "email": data.get("email", users[user_id]["email"])
    })
    return jsonify({"message": "User updated", "user_id": user_id})

# DELETE: Remove user
@app.route("/delete-user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
