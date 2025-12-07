import os

# Rename old database if it exists
if os.path.exists('db.sqlite3'):
    try:
        os.rename('db.sqlite3', 'db.sqlite3.old')
        print("✓ Renamed old database to db.sqlite3.old")
    except:
        print("✗ Could not rename database")
        print("Restart your computer and try again")
else:
    print("✓ No old database found")

print("\nNow run: python manage.py migrate")
