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
def add_entry(url: str, title : str, subtitle : str, authors: list, content: list, tags: list) -> None:
    with conn:  # assuming we have connection
        with conn.cursor() as dbcurs:
            try:
                # Insert data into the database with text arrays for authors and tags
                dbcurs.execute(f"""
                    INSERT INTO articles (url, title, subtitle, authors, content, tags) VALUES
                    ('{url}', '{title}', '{subtitle}', ARRAY{authors}::text[], ARRAY{content}::text[], ARRAY{tags}::text[]);
                """)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
def find_tag(tag : str):
    with conn: # assuming we have connection
        with conn.cursor() as dbcurs:
            try:
                dbcurs.execute(f"SELECT * FROM articles WHERE tags @> ARRAY['{tag}'];")
                results = dbcurs.fetchall()
                # result = dbcurs.fetchone() # fetch only one row
                return results
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
# get the 10 most recent articles from the data base (based on order of ID)
def get_recent_articles():
    with conn: # we have connection 
        with conn.cursor() as dbcurs:
            try:
                dbcurs.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 10")
                results = dbcurs.fetchall()         
                return results
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            
# Example call to add_entry
#add_entry('myarticle.com', "here is my article", "this article goes into the deep", ["Dmitri", "Zombie"], [["the towers have been hit again :/"], ["this is the second time this happened this week"], ["https://balsamic.web"]], ['Cool', 'Bool'])
# Example call for find_fag
#print(find_tag("Cool"))
# Example call to get_recent_articles
#print(get_recent_articles())