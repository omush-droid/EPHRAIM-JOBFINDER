import os
import sys
import time

db_path = 'db.sqlite3'

print("Attempting to delete database...")

# Try multiple times
for attempt in range(5):
    try:
        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"✓ Successfully deleted {db_path}")
            break
        else:
            print(f"✓ {db_path} doesn't exist")
            break
    except Exception as e:
        if attempt < 4:
            print(f"Attempt {attempt + 1} failed, retrying...")
            time.sleep(1)
        else:
            print(f"\n✗ Failed to delete {db_path}")
            print("\nManual steps:")
            print("1. Close ALL terminals and command prompts")
            print("2. Restart VS Code/your IDE")
            print("3. Manually delete db.sqlite3 from File Explorer")
            print("4. Run: python manage.py migrate")
            sys.exit(1)

print("\n✓ Ready! Now run: python manage.py migrate")
