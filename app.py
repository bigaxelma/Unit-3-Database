from flask import Flask, render_template, request, redirect, url_for, flash

from sample_movies import movies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# ⚠️ PROBLEM: These movies only exist in RAM (temporary memory)
# When you stop the Flask app, this data is GONE forever!

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Homepage with hero section"""
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
