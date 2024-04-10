# Fitness Spot

Fitness Spot is a web application built with Django that allows users to add their own workout routines/challenges they can
display with their friends, post to their friends. Users can also comment on posts, like posts, and reply to comments. Users 
can also search for other users by username, first name, or last name. Users can also send and receive friend requests to 
connect with other users. Users can also receive notifications for new friend requests, comments, and likes.

There is a main page where users can see posts from their friends and can also see their own posts.

## Features

- **User and custom profile**: Users can register, log in, and manage their profiles.
- **Workout routine creation**: Create workout routines with exercises, sets, reps, and weights.
- **Discussion forum (Like social media)**: Post updates, progress, and questions to engage with the community.
  - **Post to your friends**: Share workout routines and progress updates with friends.
  - **Comment on posted items**: Comment on posts to provide feedback and support.
  - **Reply to comments**: Reply to comments to engage in discussions.
- **Notification system**: Receive notifications for new friend requests, comments, and likes.
- **Add or remove friends**: Sent and receive friend requests to connect with other users.
- **Search for users**: Search for users by username, first name, or last name.

## Project Structure

The project directory structure is organized as follows:

- `fitness_spot/`: Main project directory containing settings and configurations.
- `auths/`: App for user authentication.
- `core/`: App for everything else.
- `media/`: Directory for user-uploaded files.
- `static/`: Directory for static files.
- `templates/`: Directory for HTML templates.
- `scripts/`: Directory for scripts to populate the database with initial data.
- `requirements.txt`: File containing the project dependencies.
- `manage.py`: Django's command-line utility for administrative tasks.
- `db.sqlite3`: SQLite database file.
- `README.md`: Project documentation.

## Installation
### To run the project from a Docker container, follow these steps:
1. Pull the Docker image from Docker Hub:

   ```bash
   docker pull bibishanpandey/fitness-spot
   ```

2. Run the Docker container:

   ```bash
    docker run -p 8000:8000 bibishanpandey/fitness-spot
    ```

3. Open the browser and navigate to `http://localhost:8000/` to access the application.
4. To access the admin panel, navigate to `http://localhost:8000/admin/` and log in with the following credentials:
   - Email: `admin@admin.admin`
   - Password: `admin`

### To run the project locally, follow these steps:
1. Clone the repository:

   ```bash
   git clone https://github.com/bibishan-pandey/fitness-spot.git
   ```

2. Navigate to the project directory:

   ```bash
    cd fitness-spot
   ```

3. Create and activate a virtual environment (If `venv` is not created, run both commands, otherwise run the second command only):

   ```bash
    python -m venv venv
    source venv/bin/activate
   ```
   If you are using Windows, activate the virtual environment with the following command:
   
   ```bash
    venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
    pip install -r requirements.txt
   ```

5. Create the database / Apply migrations:

   ```bash
    python manage.py migrate
   ```
   
6. Create a superuser:

   ```bash
    python manage.py createsuperuser
   ```
   
7. Populate the database with initial data:

   ```bash
    python manage.py loaddata core/fixtures/workout_types.json
    python manage.py loaddata core/fixtures/workouts.json
   ```
   When seeding the posts fixture, first run a script to copy images from the `static/images` directory to the `media/post/image` directory:
   
   ```bash
    python scripts/seed_post_data.py
    ```
   
   Then load the posts fixture:
   
   ```bash
    python manage.py loaddata core/fixtures/posts.json
    ```   

8. Run the development server:

   ```bash
     python manage.py runserver
    ```
   
9. Open the browser and navigate to `http://localhost:8000/` to access the application.
