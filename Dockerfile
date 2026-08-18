# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies for PostgreSQL client
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file (if you have one)
COPY requirements.txt .

# Install Python dependencies
# RUN pip install --no-cache-dir flask sqlalchemy psycopg2-binary
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY app_data.py .
COPY test.py .
# COPY *.ipynb .
# COPY *.md .

# Expose port 5000 (Flask default)
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=test:app
ENV FLASK_ENV=development

# Run the Flask application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
