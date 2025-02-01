
FROM python:3.10


WORKDIR /app


COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput


EXPOSE 8000

# Start the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "faq_project.wsgi:application"]
