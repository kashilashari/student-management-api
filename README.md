# 🎓 Student Management API

A RESTful Student Management API built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **Pydantic**. This project demonstrates backend development best practices including CRUD operations, request validation, database integration, dependency injection, and clean project architecture.

---

## 🚀 Features

- Student CRUD Operations
- FastAPI REST API
- SQLAlchemy ORM
- SQLite Database
- Pydantic Validation
- Dependency Injection
- Auto Increment IDs
- Persistent Database Storage
- Clean Project Architecture
- Interactive Swagger Documentation

---

## 🛠️ Technologies Used

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## 📂 Project Structure

```text
student-management-api/
│
├── routers/
│   ├── student.py
│   └── health.py
│
├── crud.py
├── database.py
├── models.py
├── schemas.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-api.git
```

### Move to Project Directory

```bash
cd student-management-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Ubuntu/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

After starting the server, visit:

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /students | Get all students |
| GET | /students/{id} | Get student by ID |
| POST | /students | Create a student |
| PUT | /students/{id} | Update a student |
| DELETE | /students/{id} | Delete a student |

---

## 🧪 Example Request

```json
{
    "name": "Muhammad Kashif",
    "age": 21,
    "department": "Computer Science",
    "cgpa": 3.80
}
```

---

## 📈 Future Improvements

- JWT Authentication
- User Login & Registration
- Department Module
- Teacher Module
- Course Module
- Attendance Management
- Role-Based Access Control
- Pagination
- Search & Filtering
- Docker Support
- Alembic Migrations
- PostgreSQL Support

---

## 👨‍💻 Author

**Muhammad Kashif**

BS Computer Science Student

Backend Developer (Python | FastAPI)

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
