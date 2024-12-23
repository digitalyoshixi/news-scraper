"""
This file will handle the connection to the postgres database aswell as provide CRUD operations
"""
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
postgrespass = os.getenv('postgrespass')
print(postgrespass)

# Connect to the database
conn = psycopg2.connect(f"DATABASE_URL=postgresql://postgres.gqujynuglauuqaicuuvy:{postgrespass}@aws-0-us-east-1.pooler.supabase.com:6543/postgres")

print(conn)
# ---- CRUD Operations ----

# Add Row to table
def add_entry(url : str, author : list[str], content : dict, tags : list[str]) -> None:
    with conn: # assuming we have connection
    	with conn.cursor() as dbcurs:
    	        try:
    	            dbcurs.execute("""
    		            INSERT INTO users (username,password) VALUES
    		            ('DANIEL','dogecoin'),
    		            ('DEMON', 'dogworm7')
    	            """)
    	        except (Exception, psycopg2.DatabaseError) as error:
    	            print(error)

