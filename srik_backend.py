import mysql.connector

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'HAREKRISHNA4',
    'database': 'cricket'
}

def connect_to_db():
    try:
        db = mysql.connector.connect(**db_config)
        print("Connected to MySQL database successfully!")
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()

connect_to_db()



def organize_tournament(db):
    try:
        cursor = db.cursor()
        tournament_name = input("Enter tournament name: ")
        tournament_id = int(input("Enter tournament ID: "))

        year = int(input("Enter tournament year: "))
        location = input("Enter tournament location: ")
        organizer_name = input("Enter organiser name: ")
        organizer_id = int(input("Enter organizer ID: "))
        contact_email=input("Enter email address:")
        query = "INSERT INTO Tournaments (tournament_id,tournament_name, year, location, organizer_id,organizer_name,contact_email) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        values = (tournament_id,tournament_name, year, location, organizer_id,organizer_name,contact_email) 
        cursor.execute(query, values)

        db.commit()  # Commit the changes

        print("Tournament organized successfully!")
    except mysql.connector.Error as err:
        print(f"Error organizing tournament: {err}")

def join_tournament(db):
    try:
        cursor = db.cursor()

        # Display available tournaments
        query = "SELECT tournament_id, tournament_name FROM Tournaments"
        cursor.execute(query)
        available_tournaments = cursor.fetchall()

        if available_tournaments:
            print("Available Tournaments:")
            for tournament in available_tournaments:
                print(f"Tournament ID: {tournament[0]}, Name: {tournament[1]}")
        else:
            print("No tournaments found.")

        # Collect team details from the user
        team_id = int(input("Enter team ID: "))
        team_name = input("Enter team name: ")
        manager_id = int(input("Enter manager ID: "))
        manager_name = input("Enter manager name: ")
        contact_email=input("Enter email_id:")
        tournament_id = int(input("Enter tournament ID: "))



        query = "INSERT INTO teams (team_id, team_name,manager_id, manager_name, contact_email,tournament_id ) VALUES (%s, %s, %s, %s, %s,%s)"
        values =  (team_id, team_name,manager_id, manager_name, contact_email,tournament_id )
        cursor.execute(query, values)


        # Insert details into Teams table (Write your SQL query here)
        # Example query: INSERT INTO Teams (team_name, manager_id) VALUES (%s, %s)
        # You'll need to adjust the query based on your table structure.

        db.commit()  # Commit the changes

        print("Team joined successfully!")
    except mysql.connector.Error as err:
        print(f"Error joining tournament: {err}")


if __name__ == "__main__":
    db = connect_to_db()

    while True:
        print("\n1. Organize a tournament\n2. Join a tournament\n3. Check scores\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            organize_tournament(db)
        elif choice == "2":
            join_tournament(db)
        elif choice == "3":
            # Implement check_scores function
            pass
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

    db.close()
