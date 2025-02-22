# Django JWT Authentication API with Product Management

🚀 A simple Django REST Framework (DRF) project with **JWT authentication** (Login & Registration) and **Product Management APIs**.

## 🔥 Features
- User Registration & Login using **JWT Tokens**
- CRUD operations for **Product Management**
- **Django Admin Panel** support
- Secure API authentication with **JWT**
- Uses **Django REST Framework (DRF)**

---

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/django-jwt-project.git
cd django-jwt-project
```

### 2️⃣ **Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django djangorestframework djangorestframework-simplejwt
```

### 3️⃣ **Setup Django Project**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create admin user
python manage.py runserver
```

---

## 🛡️ **Authentication APIs (JWT)**
### **🔹 Register a New User**
```http
POST /api/auth/register/
Content-Type: application/json
```
```json
{
  "username": "rahul",
  "email": "rahul@example.com",
  "password": "password123"
}
```

### **🔹 Get JWT Token (Login)**
```http
POST /api/auth/login/
Content-Type: application/json
```
```json
{
  "username": "rahul",
  "password": "password123"
}
```
📝 **Response:**  
```json
{
  "refresh": "refresh_token_here",
  "access": "access_token_here"
}
```

### **🔹 Refresh Access Token**
```http
POST /api/auth/token/refresh/
```
```json
{
  "refresh": "refresh_token_here"
}
```

---

## 🛆 **Product APIs (Authenticated)**
🔑 **Use Bearer Token in Headers**  
```http
Authorization: Bearer access_token_here
```

### **🔹 Create a Product**
```http
POST /api/products/
```
```json
{
  "name": "Laptop",
  "description": "Gaming laptop",
  "price": "1200.50"
}
```

### **🔹 Get All Products**
```http
GET /api/products/
```

### **🔹 Update Product (by ID)**
```http
PUT /api/products/{id}/
```

### **🔹 Delete Product (by ID)**
```http
DELETE /api/products/{id}/
```

---

## 🏋️‍♂️ **Django Admin Panel**
- Access the admin panel at **`http://127.0.0.1:8000/admin/`**
- Log in with the superuser credentials
- Manage users and products easily

---

## 🏆 **Technologies Used**
- **Django** (Backend Framework)
- **Django REST Framework (DRF)**
- **JWT Authentication (Simple JWT)**
- **SQLite (Default DB, can be changed)**

---

## 🌟 **Contribute**
Want to contribute? Feel free to fork this repository and submit a pull request! 🚀

---

## 🍿️ **Keywords for Searchability**
`django jwt` `django rest framework jwt` `drf authentication` `django login api` `django product management api` `jwt token authentication` `drf jwt login` `django api with jwt`

---
---

### **📩 Contact**
For any issues, feel free to open an [issue](https://github.com/yourusername/django-jwt-project/issues) or reach out.

---

