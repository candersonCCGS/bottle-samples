from bottle import route, run, template, request, static_file
import sqlite3
import scripts.create_database as create_database
import scripts.insert_db_data as insert_db_data
import queries

##################################################
#
# Constants
#
DATABASE_FILE = 'fuelwatch.db'


##################################################
#
# Routes for each page
#
# Home page
@route('/')
def index():
    return template('index')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Queries to create a fresh database and insert data into the database
@route('/create_db')
def create_db():
    title = "Creating Empty Database"
    success = create_database.create_db(DATABASE_FILE)
    return  template('create_database', success=success)

@route('/insert_data')
def insert_data():
    title = "Inserting Data into Database"
    result = insert_db_data.insert_table_data(DATABASE_FILE)
    return  template('insert_data', success=result)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hard coded queries that always return the same results
@route('/select_all_stations')
def select_all_stations():
    title = 'All Petrol Stations'
    description = 'The following table lists all the stations in the Fuel Watch database.'
    query = queries.SELECT_ALL_STATIONS
    return get_template(query, title, description)

@route('/select_all_areas')
def select_all_areas():
    title = 'Areas of Western Australia'
    description = 'A list of all the areas with petrol stations in Western Australia.'
    query = queries.SELECT_ALL_AREAS
    return get_template(query, title, description)

@route('/select_all_diesel')
def select_all_diesel():
    title = 'Price of Diesel'
    description = 'The price of diesel at all stations listed from cheapest to most expensive.'
    query = queries.SELECT_ALL_DIESEL
    return get_template(query, title, description)

@route('/select_stations_per_city')
def select_stations_per_city():
    title = 'Stations per City'
    description = 'The following table shows the number of stations in each city, sorted based on the number of stations.'
    query = queries.SELECT_STATIONS_PER_CITY
    return get_template(query, title, description)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Queries that require the use of a form.
# NOTE: For these queries the form is embedded in the home page
@route('/select_stations_in_area', method='POST')
def select_find_cities():
    area_value = request.forms.get('area_value')
    values = {'area': area_value }

    title = f'Stations in {area_value}'
    description = f'This page shows the number of stations in {area_value}'
    query = queries.SELECT_STATIONS_IN_AREA
    return get_template_with_parameters(query, values, title, description)

@route('/select_brands_in_region', method='POST')
def select_brands_in_region():
    brand_value = request.forms.get('brand_value')
    region_value = request.forms.get('region_value')
    values = {'brand': brand_value, 'region': region_value }

    title = f'Stations in {region_value}'
    description = f'The following table shows all the {brand_value} stations in the {region_value} region.'
    query = queries.SELECT_BRANDS_IN_REGION
    return get_template_with_parameters(query, values, title, description)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Queries that use a form on another page
@route('/select_stations_in_region')
def select_stations_in_region():
    return template('form_stations_in_region')

@route('/select_stations_in_region', method='POST')
def select_stations_in_region():
    region_value = request.forms.get('region_value')
    values = { 'region': region_value }

    title = f'Stations in {region_value}'
    description = f'The following table shows all the stations in the {region_value} region.'
    query = queries.SELECT_STATIONS_IN_REGION
    return get_template_with_parameters(query, values, title, description)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Static CSS Files
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##################################################
#
# Helper functions to run queries for each page
#
def get_db_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection

def run_query(query):
    return run_query_with_parameters(query, {})

def run_query_with_parameters(query, values):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(query, values)
    result = cursor.fetchall()

    connection.close()

    return result

def get_template(query, title='Query Results', description='This page shows the results of a query'):
    return get_template_with_parameters(query, {}, title, description)

def get_template_with_parameters(query, values, title='Query Results', description='This page shows the results of a query'):
    result = run_query_with_parameters(query, values)
    page = template('results', title=title, description=description, records=result)
    return page

##################################################
#
# Run the web server to serve up the pages
#
run(host='localhost', port=8080, reloader=True, debug=True)