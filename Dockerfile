# Use an official Python image as base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Create staticfiles directory before running collectstatic
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port Django runs on
EXPOSE 8000

# Start the Django server using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "faq_project.wsgi:application"]
