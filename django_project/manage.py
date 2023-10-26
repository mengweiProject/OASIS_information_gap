#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from util.db_pool import Database

# db1 = Database()
# db1.connect()
# conn1 = db1.get_connection()
# cursor1 = conn1.cursor()

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
