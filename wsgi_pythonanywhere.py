# WSGI Configuration for PythonAnywhere
# Save this as: /var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py
# (This file will be created automatically on PythonAnywhere, edit it there)

import os
import sys

# =========================================
# CONFIGURATION - UPDATE THESE VALUES
# =========================================
# Replace YOUR_USERNAME with your actual PythonAnywhere username
USERNAME = 'YOUR_USERNAME'
PROJECT_NAME = 'hayalisleri'
VIRTUALENV_NAME = 'hayalisleri-env'

# =========================================
# PATH CONFIGURATION
# =========================================
# Add your project directory to the sys.path
project_home = f'/home/{USERNAME}/{PROJECT_NAME}'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# =========================================
# ENVIRONMENT VARIABLES
# =========================================
# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = f'{PROJECT_NAME}.settings'

# Optional: Set secret key from environment variable
# os.environ.setdefault('DJANGO_SECRET_KEY', 'your-secret-key-here')

# =========================================
# VIRTUAL ENVIRONMENT ACTIVATION
# =========================================
# Activate virtual environment
activate_this = f'/home/{USERNAME}/.virtualenvs/{VIRTUALENV_NAME}/bin/activate_this.py'
try:
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
except FileNotFoundError:
    # If using Python 3.10+, activation might not be necessary
    # But we still need to point to the right Python
    pass

# =========================================
# DJANGO APPLICATION
# =========================================
# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# =========================================
# DEBUGGING (Remove in production)
# =========================================
# Uncomment below for debugging path issues
# print('Python version: ', sys.version)
# print('Python path: ', sys.path)
# print('Project home: ', project_home)
