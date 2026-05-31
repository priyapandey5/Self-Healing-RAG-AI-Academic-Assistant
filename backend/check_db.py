# backend/check_db.py

from database.mongo import db

print(db.name)
print(db.list_collection_names())