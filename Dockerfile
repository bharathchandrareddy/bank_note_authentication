# Use official Python image
FROM python:3.11-slim

# Set environment variables
# Prevents Python from writing .pyc files (compiled bytecode) — keeps containers cleaner.
ENV PYTHONDONTWRITEBYTECODE=1    
# Ensures that Python output is logged immediately (no buffering) — helpful for real time logging in Docker.
ENV PYTHONUNBUFFERED=1


# copy current working directory to /user/app
COPY . /user/app/

# Set working directory
WORKDIR /user/app/


# Install Python dependencies
# COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


# Set environment variables for Flask

# Tells Flask which file to run.
ENV FLASK_APP=main.py
# Makes Flask accessible outside the container.
ENV FLASK_RUN_HOST=0.0.0.0
# Enables debug mode, auto-reload, better error messages.
ENV FLASK_ENV=development

# Expose port 5000 (default for Flask) Tells Docker that your app listens on port 5000.
EXPOSE 5000

# Run Flask app
CMD ["flask", "run"]
