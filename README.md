# Project-On-Fastapi-Using-RestAPIs-With-SQLAlchemy
# FastAPI REST API with SQLAlchemy (CRUD)
This project is a backend application built using **FastAPI** that implements RESTful APIs with full **CRUD (Create, Read, Update, Delete)** operations using **SQLAlchemy ORM** for database interaction.
It demonstrates how to build a clean, scalable backend where API logic and database operations are properly separated instead of writing raw SQL or unstructured code.
---

## 🚀 Overview

This project focuses on building a real-world API system where data is stored in a database and managed through structured endpoints.
It covers:
* REST API development using FastAPI
* Database interaction using SQLAlchemy ORM
* Data validation using Pydantic
* Clean architecture with separation of concerns
---

## ⚙️ Features
* Create new records in the database
* Retrieve all records or a specific record by ID
* Update existing records
* Delete records
* ORM-based database handling (no raw SQL required)
* Automatic API documentation (`/docs`)
* Modular and maintainable code structure
---

## 🛠️ Tech Stack
* **Backend**: FastAPI
* **Language**: Python
* **ORM**: SQLAlchemy
* **Database**: SQLite (can be replaced with PostgreSQL/MySQL)
* **Validation**: Pydantic
* **Server**: Uvicorn
---

## 📂 Project Structure

```
project/
│── main.py              # Application entry point
│── database.py          # Database connection setup
│── models.py            # SQLAlchemy models (tables)
│── schemas.py           # Pydantic schemas
│── crud.py              # Database operations
│── routers/             # API routes
│── requirements.txt     # Dependencies
```
---
## 📌 API Endpoints

| Method |  Description       |
| ------ |  ----------------- |
| GET    |  Get all records   |
| GET    |  Get record by ID  |
| POST   | Create new record  |
| PUT    |  Update record     |
| DELETE |  Delete record     |

---

## ▶️ How to Run
1. Run the server:

   ```
   uvicorn main:app --reload
   ```
2. Open API docs:

   ```
   http://127.0.0.1:8000/docs
   ```
---

## 🧠 What This Project Teaches
Most beginners either:
* Write raw SQL everywhere
* Or mix database logic directly inside routes
  
This project avoids both mistakes by:
* Using SQLAlchemy ORM for structured database interaction
* Separating models, schemas, and CRUD logic
* Keeping routes clean and focused only on request handling
---

## Conclusion

This project demonstrates how to build a structured and scalable backend using FastAPI with SQLAlchemy. It provides a solid foundation for understanding how APIs interact with databases in real-world applications.
