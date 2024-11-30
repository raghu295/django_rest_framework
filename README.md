# Django REST Framework Project

This is a Django REST Framework project that includes user authentication, password reset via email.

## Requirements

Make sure you have the following installed:

- Python 3.8+
- Django 5.1.1
- Django REST Framework
- Django CORS Headers
- Django Dotenv
- Django REST Framework SimpleJWT
- PyJWT
- SQLParse
- TZData

## Installation

1. **Clone the repository:**

   git clone https://github.com/your-username/django_rest_framework.git
   cd django_rest_framework

2. **Create a virtual environment:**
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install the dependencies:**
   pip install -r requirements.txt

4. **Set up environment variables:**
    Create a .env file in the root directory and add the following:
    EMAIL_USER=your_email@example.com
    EMAIL_PASS=your_email_password_or_app_password
    EMAIL_FROM=your_email@example.com

5. **Run Migrations:**
    python manage.py migrate

6. **Create a SuperUser:**
   python manage.py createsuperuser

7. **Run the Development Server:**
   python manage.py runserver


**Features**
User registration and login
Password reset via email
JWT authentication


**Usage**
1. *User Registration*
Endpoint: /api/user/register/
Method: POST
Payload:
{
    "email": "user@example.com",
    "name": "User Name",
    "password": "password123",
    "password2": "password123",
    "tc": true
}

2. *User Login*
Endpoint: /api/user/login/
Method: POST
Payload:

{
    "email": "user@example.com",
    "password": "password123"
}

4. *Password Reset*
Endpoint: /api/user/reset-password/
Method: POST
Payload:
{
    "email": "user@example.com"
}



