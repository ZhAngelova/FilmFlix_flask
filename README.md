Project Title: FilmFlix

Description:

FilmFlix is a web application built with Flask, a Python web framework, designed to manage a database of films. It provides users with a platform to browse, add, update, and delete film records. The application allows users to view a list of films with details such as title, release year, rating, duration, and genre. Users can also add new films to the database, update existing film records, and delete films from the collection.

Features:

Browse a list of films with detailed information.
Add new films to the database.
Update existing film records with updated information.
Delete films from the collection.
Responsive design for seamless user experience across devices.
Technologies Used:

Flask: Python web framework for building the backend logic and routing.
SQLite: Lightweight relational database for storing film records.
HTML/CSS: Front-end markup and styling, with Bootstrap for responsive design.
Jinja2: Template engine for rendering dynamic content in HTML templates.
JavaScript: Client-side scripting for interactive features (if applicable).
Purpose:

The purpose of FilmFlix is to provide a simple and intuitive interface for managing a collection of films. Whether you're a film enthusiast looking to catalog your favorite movies or a film curator managing a database for a film festival, FilmFlix offers the tools you need to organize and maintain your film records efficiently.

Quick Start Guide:

1. Prerequisites

Python 3.12 or higher

pip (Python package manager)

virtualenv (Recommended for dependency management)

2. Setup & Run

a) Open Terminal in VS Code (in my case)

Press Ctrl + `  to open the integrated terminal.

b) Navigate to Project Folder

cd path/to/FilmFlix_Flask

c) Activate Virtual Environment

Windows:

virtenv\Scripts\activate

macOS/Linux:

source virtenv/bin/activate

d) Install Dependencies

pip install -r requirements.txt

e) Run Flask App

python app.py

Open http://127.0.0.1:5000/ in your browser.

3. Troubleshooting

Flask module not found? Run: pip install flask

Port 5000 already in use? Run: python app.py --port=5001

App not displaying correctly? Ensure templates/index.html exists.

4. Stop the App

Press CTRL + C in the terminal to stop the server.

5. Restart Flask (If Needed)

python app.py

License

MIT License



