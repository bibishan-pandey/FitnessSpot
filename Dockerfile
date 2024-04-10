# Use an official Python runtime as a parent image
FROM python:3.11.8

# Set environment variables for Python and Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for the Django superuser
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@admin.admin
ENV DJANGO_SUPERUSER_PASSWORD=admin

# Expose port 8000 to allow external access to the Django application
EXPOSE 8000

# Remove the default SQLite database
RUN rm -rf /app/db.sqlite3

# Run migrations and start the Django development server
RUN python manage.py migrate
RUN python manage.py createsuperuser --noinput
RUN python manage.py loaddata core/fixtures/workout_types.json
RUN python manage.py loaddata core/fixtures/workouts.json
RUN python scripts/seed_post_data.py
RUN python manage.py loaddata core/fixtures/posts.json

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
