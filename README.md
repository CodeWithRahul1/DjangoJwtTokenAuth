# Django JWT Authentication API with Product Management

🚀 A simple Django REST Framework (DRF) project with **JWT authentication** (Login & Registration) and **Product Management APIs**.

## 🔥 Features
- User Registration & Login using **JWT Tokens**
- CRUD operations for **Product Management**
- **Django Admin Panel** support
- Secure API authentication with **JWT**
- Uses **Django REST Framework (DRF)**
- Implements **Rate Limiting, Load Balancing, Caching, and Circuit Breaking**

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
pip install django djangorestframework djangorestframework-simplejwt django-ratelimit django-cacheops
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

## 🚶 **Product APIs (Authenticated)**
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

## 🏋️ **Django Admin Panel**
- Access the admin panel at **`http://127.0.0.1:8000/admin/`**
- Log in with the superuser credentials
- Manage users and products easily

---

## 💪 **Performance Enhancements**

### 1. 📊 **Rate Limiting**
Implemented using `django-ratelimit` to prevent excessive API calls:
```python
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', method=['GET', 'POST'], block=True)
def my_view(request):
    return Response({"message": "This endpoint is rate-limited."})
```

### 2. 🌌 **Load Balancing**
- Can be achieved using **NGINX** or **AWS ELB**.
- Helps distribute traffic across multiple Django instances.

### 3. 🔐 **Caching**
Implemented using **django-cacheops** for caching database queries:
```python
CACHEOPS = {
    'products.product': {'ops': 'all', 'timeout': 60*15},  # Cache for 15 minutes
}
```

### 4. 🛡 **Circuit Breaking**
Implemented using try-except to prevent failures from cascading:
```python
from django.http import JsonResponse

def safe_api_call():
    try:
        response = requests.get("https://external-api.com/data", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return JsonResponse({"error": "Service Unavailable"}, status=503)
```

---

## 🏆 **Technologies Used**
- **Django** (Backend Framework)
- **Django REST Framework (DRF)**
- **JWT Authentication (Simple JWT)**
- **SQLite (Default DB, can be changed)**
- **NGINX (For Load Balancing)**
- **Redis (For Caching)**

---

## 🌟 **Contribute**
Want to contribute? Feel free to fork this repository and submit a pull request! 🚀

---

## 🍿 **Keywords for Searchability**
`django jwt` `django rest framework jwt` `drf authentication` `django login api` `django product management api` `jwt token authentication` `drf jwt login` `django api with jwt` `django rate limiting` `django caching` `django circuit breaking`

---

### **📩 Contact**
For any issues, feel free to open an [issue](https://github.com/yourusername/django-jwt-project/issues) or reach out.

---

