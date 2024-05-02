import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('your_database_name.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the ballbyball table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ballbyball (
        ball_id INTEGER PRIMARY KEY,
        match_id INTEGER,
        inning INTEGER,
        over_number INTEGER,
        ball_number INTEGER,
        batter_id INTEGER,
        bowler_id INTEGER,
        runs_scored INTEGER DEFAULT 0,
        extras INTEGER DEFAULT 0,
        wicket_type VARCHAR(50) DEFAULT 'NONE',
        fielder_id INTEGER DEFAULT NULL,
        FOREIGN KEY (match_id) REFERENCES matches(match_id),
        FOREIGN KEY (batter_id) REFERENCES players(player_id),
        FOREIGN KEY (bowler_id) REFERENCES players(player_id),
        FOREIGN KEY (fielder_id) REFERENCES players(player_id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
