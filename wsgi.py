# wsgi.py
import sys
import os

# The following two lines are crucial for allowing Gunicorn to find your app.py file
# They ensure that your project's directory is in the Python path.
sys.path.insert(0, os.path.dirname(__file__))

# Import the app instance from your main application file
from genai import app

# This part is optional but useful for local testing of the wsgi file
if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)