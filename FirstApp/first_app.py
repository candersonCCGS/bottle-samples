from bottle import route, run, template, static_file, request
import sqlite3
import scripts.create_database as create_db
import scripts.insert_data as db_insert

@route('/')
def index():
    return template('index')

@route('/hello')
def hello():
    return template('hello', name='James')

@route('/customers')
def customers():
    customer_list = [
        {'first_name': 'James', 'last_name': 'Smith'},
        {'first_name': 'John', 'last_name': 'Chalmers'},
        {'first_name': 'Jane', 'last_name': 'Peterson'}
    ]
    return template('customers', customers=customer_list)

@route('/create_database')
def create_database():
    create_db.create_empty_database('teams.db')
    return template('database_create')

@route('/insert_data')
def insert_data():
    db_insert.insert_sample_data('teams.db')
    return template('database_insert')

@route('/select_all_teams')
def select_all_teams():
    conn = sqlite3.connect('teams.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = 'SELECT * FROM Team'
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return template('results', records=result, title='All Teams')

@route('/select_players_and_team')
def select_all_teams():
    conn = sqlite3.connect('teams.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = '''
            SELECT Player.first_name, Player.last_name, Team.name 
            FROM Player, Team
            WHERE Player.team_id = Team.team_id
            '''
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return template('results', records=result, title='All Teams')

@route('/select_team_players', method='POST')
def select_player_team():
    name_value = request.forms.get('name_value')
    values = {'team_name': name_value }

    title = f'Players for the team {name_value}'

    conn = sqlite3.connect('teams.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = '''
            SELECT Player.first_name, Player.last_name, Team.name 
            FROM Player, Team
            WHERE Player.team_id = Team.team_id
              AND Team.name = :team_name
            '''
    cursor.execute(query, values)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return template('results', records=result, title=title)

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)