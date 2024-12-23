"""
This file will handle the connection to the postgres database aswell as provide CRUD operations
"""
import psycopg2
import os
from dotenv import load_dotenv
import json
load_dotenv()
postgrespass = os.getenv('postgrespass')
# Connect to the database
try:
    conn = psycopg2.connect(f"postgresql://postgres.gqujynuglauuqaicuuvy:{postgrespass}@aws-0-us-east-1.pooler.supabase.com:6543/postgres")
    print("Connected to the data base sucessfully!")
except Exception as e:
    print("Unable to connect to the database.")
    print(e)

# Data nornalization
def listtodict(inplist : list):
    retdict = dict()
    for i in range(len(inplist)):
        retdict[i] = inplist[i]
    return retdict

# ---- CRUD Operations ----

# Add Row to table
def add_entry(url: str, authors: list, content: dict, tags: list) -> None:
    with conn:  # assuming we have connection
        with conn.cursor() as dbcurs:
            try:
                # Insert JSON object into the database
                dbcurs.execute(f"""
                    INSERT INTO articles (url, authors, content, tags) VALUES
                    ('{url}', '{json.dumps(listtodict(authors))}'::jsonb, '{json.dumps(content)}'::jsonb, '{json.dumps(listtodict(tags))}');
                """)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

# Example call to add_entry
add_entry('marimo', ["Dmitri", "Zombie"], {'0': ["the towers have been hit again :/"]}, ['Cool', 'Fun'])
