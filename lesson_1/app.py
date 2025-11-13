from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Movie
from lesson_1.sample_movies import movies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# ⚠️ PROBLEM: These movies only exist in RAM (temporary memory)
# When you stop the Flask app, this data is GONE forever!

# ============================================================================
# ROUTES
# ============================================================================

# DATA BASE CONFIGURATION
#SQlite database will be stored in instance/cinematch.db
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite://cinematch.db'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize the databse
db.init_app(app)

# DATABASE INITIALIZATION
def create_table():
    """Create all database tables, this runs once to set up the database"""
    with app.app_context():
        db.create+all()
        print("databse tables created")


def load_initial_movies():
    with app.app_context():
        if Movie.query.count() == 0:
            print("loading initial movies!") 
            movies = [
                Movie(
                    title = "Inception",
                    year = 2010,
                    genre = 'Sci-Fi',

                )
            ]

@app.route('/')
def index():
    """Homepage with hero section"""
    movies = Movie.query.limit(4).all
    return render_template('index.html', movies=movies)


@app.route('/movies')
def movies_list():
    """
    Display all movies
    
    TODO (Later in Unit 3): Change this to query from database instead of list
    """
    return render_template('movies.html', movies=movies)


@app.route('/about')
def about():
    """About CineMatch page"""
    return render_template('about.html')


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('errors/500.html'), 500


# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == '__main__':
    # Debug mode: Shows errors and auto-reloads on code changes
    app.run(debug=True, host='0.0.0.0', port=5000)
