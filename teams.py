import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('your_database_name.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the teams table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        team_id INTEGER PRIMARY KEY,
        team_name VARCHAR(255),
        manager_id INTEGER,
        manager_name VARCHAR(255),
        contact_email VARCHAR(255),
        tournament_id INTEGER,
        FOREIGN KEY (tournament_id) REFERENCES Tournaments(tournament_id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
