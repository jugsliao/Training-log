# Training Log Web App

The Training Log Web App is a Django-based application that allows users to track their fitness goals and log their workout progress. Users can register and log in to the app, create goals that are displayed on the dashboard, and maintain a fitness log to add, edit, and delete workout entries.

## Features

- **User Registration and Login**: Users can create an account and log in to the web app using their credentials. This ensures secure access to their personal training log data.
- **Goal Creation**: Users can set fitness goals, such as running a marathon or losing a certain amount of weight. Once a goal is created, it is displayed on the user's dashboard as a reminder and motivation.
- **Dashboard**: After logging in, users are presented with a personalized dashboard that provides an overview of their goals and progress. They can easily view their goals, completed workouts, and overall progress.
- **Fitness Log**: Users can maintain a fitness log to track their workout activities. They can add new entries to record details such as exercise type, duration, intensity, and notes. Entries can be edited or deleted as needed.

## Installation

To run the Training Log Web App locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Navigate to the project directory: `cd training-log-app`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Start the local development server: `python manage.py runserver`
8. Access the web app at `http://localhost:8000` in your browser.

Note: Ensure that you have Python and Django installed on your machine before proceeding with the installation.

## Usage

Once the Training Log Web App is running, you can perform the following actions:

1. **User Registration**: Click on the "Register" link on the homepage to create a new account. Provide the required information and submit the form.

2. **User Login**: After registration, click on the "Login" link on the homepage and enter your credentials to log in to your account.

3. **Create a Goal**: Once logged in, navigate to the dashboard and click on the "Create Goal" button. Enter the details of your fitness goal and submit the form. The goal will be displayed on your dashboard.

4. **Fitness Log Entries**: On the dashboard, you can add new workout entries by clicking on the "Add Entry" button. Fill in the details of your workout, such as exercise type, duration, intensity, and any notes. Submit the form to add the entry to your fitness log. Existing entries can be edited or deleted as needed.


