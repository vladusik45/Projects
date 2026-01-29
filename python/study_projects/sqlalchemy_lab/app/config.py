import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:5432@localhost/python")
