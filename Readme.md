FAQ Management System
Docker Pull Command: docker pull shivam00300/faq_project-web

This project is a Django-based web application for managing Frequently Asked Questions (FAQs) with multilingual support. It includes a WYSIWYG editor for answers, dynamic translations, and caching to improve performance.

Features

FAQ Management: Store questions and answers, with support for multilingual translations.
WYSIWYG Editor: Use django-ckeditor to format answers with rich text.
Multilingual Support: Translations are automated via the Google Translate API or googletrans.
Caching: Translations are cached using Redis for faster retrieval.
REST API: Expose FAQs through an API with language selection via query parameters.
Admin Panel: Easily manage FAQs via the Django admin interface.
Testing: Unit tests are written with pytest to ensure functionality.
Installation

Follow these steps to set up the project on your local machine.
Prerequisites
Python 3.x
Django 5.x
Redis (for caching)
1. Clone the Repository
git clone https://github.com/yourusername/faq-management.git
cd faq-management

2. Install Dependencies
Create a virtual environment and install the necessary dependencies.
python -m venv venv
pip install -r requirements.txt

3. Set Up Redis
Ensure Redis is installed and running. You can install Redis locally or use Docker.
To start Redis using Docker:
docker run --name redis-container -p 6379:6379 -d redis

4. Apply Migrations
Run the following command to set up the database:
python manage.py migrate

5. Create a Superuser (for Admin Panel)
Create a superuser to access the Django admin panel:
python manage.py createsuperuser
Follow the prompts to set up your superuser.

6. Run the Development Server
Start the Django development server:
python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/.
API Usage

The FAQ API allows users to fetch FAQs in different languages. Use the lang query parameter to specify the language.
1. Fetch FAQs in English (default)
curl http://localhost:8000/api/faqs/
2. Fetch FAQs in Hindi
curl http://localhost:8000/api/faqs/?lang=hi
3. Fetch FAQs in Bengali
curl http://localhost:8000/api/faqs/?lang=bn
Admin Panel

To manage FAQs, navigate to the Django admin interface at http://127.0.0.1:8000/admin/. Use the superuser credentials you created earlier to log in and manage FAQs.
Testing

Run the tests with pytest:
pytest
This will execute unit tests to ensure the correctness of your application.

Code Quality

In this project, I've adhered to PEP8 guidelines and best practices to ensure clean, readable, and maintainable code. Here’s how it has been implemented:
1. PEP8 Compliance
The code follows PEP8 standards for indentation, spacing, and line length to enhance readability.
I’ve used meaningful variable and method names, ensuring clarity and simplicity.
2. Readability
I have organized the code into logical sections (models, views, API, etc.) to maintain separation of concerns and clarity.
Code is formatted properly with consistent indentation, blank lines, and comments where necessary to explain non-obvious logic.
Used docstrings for classes and methods to provide a better understanding of their purpose and functionality.
3. Modularity
The project structure is modular, with separate files for each part of the application (e.g., models, views, serializers, etc.).
I’ve created reusable functions and methods for common tasks, reducing redundancy.
The use of Django's built-in features (like models, serializers, and views) enhances modularity by leveraging reusable components.
4. Code Quality Tools
I have used flake8 for linting to check for PEP8 compliance and catch any issues early.
The code is free of unnecessary complexity and is optimized for performance where needed.

Deployment

The project has been deployed using Docker. To deploy it on Heroku, follow these steps (still in progress):
Create a Dockerfile and docker-compose.yml.
Push the application to Heroku (future deployment task).

Contribution Guidelines

Fork the repository and create a new branch.
Make your changes and ensure all tests pass.
Submit a pull request with a clear explanation of your changes.

Git Commit Guidelines

Use the following convention for your commit messages:
feat: Add new features
fix: Fix bugs
docs: Update documentation
Example commit message:
feat: Add multilingual FAQ model
