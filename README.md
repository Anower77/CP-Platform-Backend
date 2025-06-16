# CP Platform

A Django-based Competitive Programming Platform with user authentication, problem management, dashboard features, and a browsable API with Swagger documentation.

## Features

- User authentication and registration
- Problem listing and management
- Dashboard for tracking problem status and bookmarks
- Topic and contest management
- RESTful API with Swagger (OpenAPI) documentation



## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Swagger API Docs: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
   - Redoc API Docs: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## API Documentation

- **Swagger UI:** `/swagger/`
- **Redoc:** `/redoc/`
- **OpenAPI JSON:** `/swagger.json`
- **OpenAPI YAML:** `/swagger.yaml`

## Main Dependencies

- Django==5.2
- djangorestframework
- drf-yasg (Swagger/OpenAPI)
- djangorestframework_simplejwt (JWT Auth)
- django-filter

(See `requirements.txt` for the full list.)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the BSD License. 