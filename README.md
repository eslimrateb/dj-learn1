# 📝 Blog Backend System

A backend system for a blog application built using **Django** and **SQLite**. This project provides core features such as user authentication, content management (posts, categories, comments), and an admin interface.

---

## 🚀 Technologies Used

- **Python**
- **Django**
- **SQLite** (default Django DB)
- **Django ORM**
- **HTML/CSS (for admin interface)**

---

## 🔧 Features

- ✅ User Registration, Login, Logout (Authentication)
- ✅ Permissions and Access Control
- ✅ CRUD operations for:
  - Posts
  - Categories
  - Comments
- ✅ Django Admin Panel for managing content and users
- ✅ Structured using Django's **MVT** architecture
- ✅ Clean code using Django best practices

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/blog-backend.git
   cd blog-backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the admin panel**
   Visit: `http://127.0.0.1:8000/`

---

## 📁 Project Structure (Simplified)
```
blog-backend/
│
├── blog/                 # App containing models, views, urls
├── blog_project/         # Main project settings and URLs
├── db.sqlite3            # Default database
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

