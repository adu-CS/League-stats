import sqlite3

conn = sqlite3.connect('database.sqlite')
print("Connected to database successfully")

def organize_tournament(conn):
    try:
        cursor = conn.cursor()
        tournament_name = input("Enter tournament name: ")
        tournament_id = int(input("Enter tournament ID: "))
        year = int(input("Enter tournament year: "))
        location = input("Enter tournament location: ")
        organizer_name = input("Enter organizer name: ")
        organizer_id = int(input("Enter organizer ID: "))
        contact_email = input("Enter email address:")
        
        # SQLite uses different syntax for parameterized queries
        query = """INSERT INTO Tournaments 
                    (tournament_id, tournament_name, year, location, organizer_id, organizer_name, contact_email) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)"""
        values = (tournament_id, tournament_name, year, location, organizer_id, organizer_name, contact_email)
        cursor.execute(query, values)

        conn.commit()  # Commit the changes

        print("Tournament organized successfully!")
    except sqlite3.Error as err:
        print(f"Error organizing tournament: {err}")

if __name__ == '__main__':
    # Connect to SQLite database
    conn = sqlite3.connect("database.sqlite")
    if conn is not None:
        # Create table if not exists
        create_table_sql = """CREATE TABLE IF NOT EXISTS Tournaments (
                                tournament_id INTEGER PRIMARY KEY,
                                tournament_name TEXT NOT NULL,
                                year INTEGER NOT NULL,
                                location TEXT NOT NULL,
                                organizer_id INTEGER NOT NULL,
                                organizer_name TEXT NOT NULL,
                                contact_email TEXT NOT NULL
                            );"""
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

        # Organize tournament
        organize_tournament(conn)
conn.close()
