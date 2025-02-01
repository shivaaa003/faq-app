FAQ Management System

Docker Pull Command

To pull the Docker image, use the following command:

<pre> docker pull shivam00300/faq_project-web </pre>
Overview

This project is a Django-based web application for managing Frequently Asked Questions (FAQs) with multilingual support. It includes a WYSIWYG editor for answers, dynamic translations, and caching to improve performance.


Features

FAQ Management: Store questions and answers with support for multilingual translations.


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
Clone the repository to your local machine:
<pre>https://github.com/shivaaa003/faq-app.git</pre>

2. Install Dependencies
Create a virtual environment and install the necessary dependencies:
<pre>python -m venv venv
pip install -r requirements.txt</pre>
3. Set Up Redis
Ensure Redis is installed and running. You can install Redis locally or use Docker.
To start Redis using Docker:
<pre>docker run --name redis-container -p 6379:6379 -d redis</pre>
4. Apply Migrations
Run the following command to set up the database:
<pre>python manage.py migrate</pre>
5. Create a Superuser (for Admin Panel)
Create a superuser to access the Django admin panel:
<pre>python manage.py createsuperuser</pre>
Follow the prompts to set up your superuser.
6. Run the Development Server
Start the Django development server:
<pre>python manage.py runserver</pre>
The application will be accessible at http://127.0.0.1:8000/.
API Usage

The FAQ API allows users to fetch FAQs in different languages. Use the lang query parameter to specify the language.
Example Requests:
Fetch FAQs in English (default):
<pre>curl http://localhost:8000/api/faqs/</pre>
Fetch FAQs in Hindi:
<pre>curl http://localhost:8000/api/faqs/?lang=hi</pre>
Fetch FAQs in Bengali:
<pre>curl http://localhost:8000/api/faqs/?lang=bn</pre>
Admin Panel

To manage FAQs, navigate to the Django admin interface at http://127.0.0.1:8000/admin/. Use the superuser credentials you created earlier to log in and manage FAQs.
Testing

Run the tests with pytest:
<pre>pytest</pre>
This will execute unit tests to ensure the correctness of your application.
Code Quality

In this project, I’ve adhered to PEP8 guidelines and best practices to ensure clean, readable, and maintainable code. Here’s how it has been implemented:
1. PEP8 Compliance:
The code follows PEP8 standards for indentation, spacing, and line length to enhance readability.
Meaningful variable and method names are used to ensure clarity and simplicity.
2. Readability:
Code is organized into logical sections (models, views, API, etc.) to maintain separation of concerns and clarity.
Consistent indentation, blank lines, and comments have been used where necessary to explain non-obvious logic.
Docstrings have been added to classes and methods to provide a better understanding of their purpose and functionality.
3. Modularity:
The project is structured with separate files for each part of the application (e.g., models, views, serializers, etc.).
Reusable functions and methods have been created for common tasks to reduce redundancy.
4. Code Quality Tools:
flake8 has been used for linting to check for PEP8 compliance and catch any issues early.
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


<img width="1440" alt="Screenshot 2025-02-02 at 3 00 46 AM" src="https://github.com/user-attachments/assets/7413f7c6-f072-4a8b-95e8-b41017b22cbc" />
<img width="1440" alt="Screenshot 2025-02-02 at 3 00 08 AM" src="https://github.com/user-attachments/assets/aa00ba77-1528-4c60-b8c0-af4c04cea3c8" />
<img width="1440" alt="Screenshot 2025-02-02 at 1 27 26 AM" src="https://github.com/user-attachments/assets/48392bd6-b708-402c-b27d-a2af0964580e" />
