import sqlite3

# Define the SQLite database name
dbname = 'stamps.db'

# Connect to the SQLite database (the database file will be created if it does not exist)
conn = sqlite3.connect(dbname)

# Create a new cursor object to execute SQL statements
cur = conn.cursor()

# Define the SQL statement for creating a new table called 'stamps'
create_table_sql = """
CREATE TABLE IF NOT EXISTS stamps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stampname TEXT NOT NULL,
    stampvalue TEXT NOT NULL
);
"""

# Execute the SQL statement to create the table
cur.execute(create_table_sql)

# Commit the changes to our database
conn.commit()

# Close the connection to the database
conn.close()

print(f"Database '{dbname}' created and table 'stamps' set up successfully.")
