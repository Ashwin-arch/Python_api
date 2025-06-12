# Python_api
# 🧩 Flask REST API – User Management

A simple REST API built using Python's Flask framework for managing user data. This API supports basic CRUD operations: **Create, Read, Update, and Delete**.

---

## 🚀 Features

- 📥 Create a user (`POST`)
- 🔍 Get user by ID (`GET`)
- 🛠️ Update user details (`PUT`)
- 🗑️ Delete user (`DELETE`)

---

## 🧰 Technologies

- Python 3.x
- Flask

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-user-api.git
cd flask-user-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If `requirements.txt` is not present, install Flask manually:
> ```bash
> pip install Flask
> ```

### 3. Run the Flask App

```bash
python app.py
```

Server will start at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔗 API Endpoints

### ➤ `GET /get-user/<user_id>`

Retrieve user details by ID.

**Example:**
```bash
curl http://localhost:5000/get-user/1
```

---

### ➤ `POST /create-user`

Create a new user.

**Request Body:**
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/create-user \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "email": "jane@example.com"}'
```

---

### ➤ `PUT /update-user/<user_id>`

Update existing user info.

**Partial Update Body Example:**
```json
{
  "name": "Updated Name"
}
```

**Example:**
```bash
curl -X PUT http://localhost:5000/update-user/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name"}'
```

---

### ➤ `DELETE /delete-user/<user_id>`

Delete a user.

**Example:**
```bash
curl -X DELETE http://localhost:5000/delete-user/1
```

---

## 📁 Sample Code Overview

```python
users = {
    "1": {"name": "John Doe", "email": "john.doe@example.com"}
}
```

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Made with ❤️ by **Your Name**  
GitHub: [@your-username](https://github.com/your-username)

---

## ⭐️ Support

If this helped you, give the repo a ⭐ on GitHub and feel free to fork or contribute!
