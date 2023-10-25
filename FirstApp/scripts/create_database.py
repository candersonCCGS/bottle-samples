import sqlite3

def create_empty_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print('Creating empty database')
    # Update database settings
    print('Update PRAGMA to support foreign keys')
    cursor.execute('PRAGMA foreign_keys = ON')

    # Drop tables if they exist to allow new tables to be created
    print('Drop tables if they exist')
    cursor.execute('DROP TABLE IF EXISTS Player;')
    cursor.execute('DROP TABLE IF EXISTS Team;')

    # Create tables
    print('Create Team table')
    cursor.execute('''CREATE TABLE Team 
                            (team_id INTEGER PRIMARY KEY,
                            name varchar(20) NOT NULL,
                            colour varchar(10));''')

    print('Create Player table')
    cursor.execute('''CREATE TABLE Player 
                            (player_id INTEGER PRIMARY KEY,
                            first_name varchar(20) NOT NULL,
                            last_name varchar(20) NOT NULL,
                            team_id INTEGER,
                            FOREIGN KEY (team_id) REFERENCES Team(team_id));''')

    conn.commit()
    cursor.close()
    conn.close()
    print('Empty database created')