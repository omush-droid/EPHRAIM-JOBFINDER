import os
import time
import sys

db_path = 'db.sqlite3'

if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print(f"✓ Deleted {db_path}")
    except PermissionError:
        print(f"✗ Cannot delete {db_path} - file is locked")
        print("\nClose all programs using the database:")
        print("- Django server (Ctrl+C)")
        print("- DB Browser or SQLite viewers")
        print("- VS Code/PyCharm terminals")
        print("\nThen run this script again.")
        sys.exit(1)
else:
    print(f"✓ {db_path} doesn't exist")

print("\nNow run: python manage.py migrate")
