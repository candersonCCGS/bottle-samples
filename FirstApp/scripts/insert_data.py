import sqlite3

def insert_sample_data(database_name):
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print('Inserting data into database')

    print('Inserting data into Team table')
    cursor.execute('INSERT INTO Team (team_id, name, colour) VALUES (1, "Dolphins", "blue");')
    cursor.execute('INSERT INTO Team (team_id, name, colour) VALUES (2, "Sharks", "green");')
    cursor.execute('INSERT INTO Team (team_id, name) VALUES (3, "Whales");')

    print('Inserting data into Team table')
    cursor.execute('INSERT INTO Player (player_id, first_name, last_name, team_id) VALUES (11, "James", "Smith", 1);')
    cursor.execute('INSERT INTO Player (player_id, first_name, last_name, team_id) VALUES (12, "Sandra", "Peters", 2);')
    cursor.execute('INSERT INTO Player (player_id, first_name, last_name, team_id) VALUES (13, "Richard", "Jones", 1);')

    conn.commit()
    cursor.close()
    conn.close()
    print('Data inserted into database')
