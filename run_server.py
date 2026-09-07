#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(project_dir, 'futurproctor'))

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'futurproctor.settings')

# Setup Django
django.setup()

# Now run the migration and server
from django.core.management import call_command

print("Running migrations...")
call_command('migrate')

print("\nStarting Django development server...")
print("Access the application at: http://127.0.0.1:8000/")
call_command('runserver', '0.0.0.0:8000')
