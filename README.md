# Fitness Spot

Fitness Spot is a web application built with Django that allows users to track their workouts, nutrition, progress, and engage with a community of fitness enthusiasts.

## Features

- **Authentication**: Users can register, log in, and manage their profiles.
- **Workout Tracking**: Log workouts with details such as activity type, duration, distance, and calories burned.
- **Nutrition Tracking**: Track daily nutrition intake with meal types and food items.
- **Progress Tracking**: Monitor progress with weight, body fat percentage, measurements, and fitness assessments.
- **Community Interaction**: Share posts and engage with other users through comments.
- **Administration**: Admin interface for managing users, content, and site settings.

## Project Structure

The project directory structure is organized as follows:

- `fitness_spot/`: Main project directory containing settings and configurations.
- `authentication/`: App for user authentication.
- `workout_tracking/`: App for workout tracking functionality.
- `nutrition_tracking/`: App for nutrition tracking functionality.
- `progress_tracking/`: App for progress tracking functionality.
- `community/`: App for community interaction.
- `administration/`: App for administration interface.

## Installation

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

8. Run the development server:

   ```bash
     python manage.py runserver
    ```
   
9. Open the browser and navigate to `http://localhost:8000/` to access the application.
