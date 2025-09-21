# Task Collaboration Web App

A Django-based web application for collaborative task management.

## Features
- User signup/login (email + password)
- Create, assign, and update tasks
- Dashboard for created and assigned tasks
- Filter/sort tasks, CSV export, analytics
- Deployed on a free platform (Render/Railway/PythonAnywhere)

## Local Setup

1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd Task_APP
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin):
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```
7. Access the app at [http://localhost:8000](http://localhost:8000)

## Deployment
- Use the provided `Procfile` and `requirements.txt` for deployment on Render, Railway, or PythonAnywhere.
- Set environment variable `DJANGO_SETTINGS_MODULE=taskwebapp.settings` if needed.

## License
MIT
