import sqlite3

def create_matches_table():
    try:
        # Establish a connection to the SQLite database (or create a new one)
        conn = sqlite3.connect('my_matches.db')

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        # Execute the CREATE TABLE statement for the matches table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS matches (
                match_id INTEGER PRIMARY KEY,
                tournament_id INTEGER NOT NULL,
                team1_id INTEGER NOT NULL REFERENCES Teams(team_id),
                team2_id INTEGER NOT NULL REFERENCES Teams(team_id),
                match_date TEXT NOT NULL,
                venue TEXT NOT NULL,
                result TEXT,
                winning_team_id INTEGER REFERENCES Teams(team_id),
                losing_team_id INTEGER REFERENCES Teams(team_id)
            )
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Matches table created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating matches table: {e}")

def add_match(db):
    try:
        cursor = db.cursor()

        # Collect match details from the user
        match_id = int(input("Enter match ID: "))
        tournament_id = int(input("Enter tournament ID: "))
        team1_id = int(input("Enter team 1 ID: "))
        team2_id = int(input("Enter team 2 ID: "))
        match_date = input("Enter match date (YYYY-MM-DD): ")
        venue = input("Enter venue: ")

        # Allow NULL values for result, winning_team_id, and losing_team_id
        result = None
        winning_team_id = None
        losing_team_id = None

        # Prompt user for result only if match is over
        match_over = input("Is the match over? (yes/no): ").lower()
        if match_over == "yes":
            result = input("Enter match result: ")
            winning_team_id = input("Enter winning team ID: ")
            losing_team_id = input("Enter losing team ID: ")

        query = "INSERT INTO matches (match_id, tournament_id, team1_id, team2_id, match_date, venue, result, winning_team_id, losing_team_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (match_id, tournament_id, team1_id, team2_id, match_date, venue, result, winning_team_id, losing_team_id)
        cursor.execute(query, values)

        db.commit()  # Commit the changes

        print("Match details added successfully!")
    except sqlite3.Error as err:
        print(f"Error adding match details: {err}")

# Example usage
create_matches_table()
db_connection = sqlite3.connect('my_matches.db')
add_match(db_connection)
db_connection.close()
