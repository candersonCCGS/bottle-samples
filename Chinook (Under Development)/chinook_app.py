from bottle import route, run, template, request, static_file
import sqlite3
# import scripts.create_database as create_database
# import scripts.insert_db_data as insert_db_data
import queries

##################################################
#
# Constants
#
DATABASE_FILE = 'Chinook.sqlite'

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Routes to mainm subsections of website
@route('/albums')
def albums():
    return template('albums')

@route('/customers')
def customers():
    return template('customers')

@route('/orders')
def orders():
    return template('orders')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Queries to find information about Albums
@route('/select_all_albums')
def select_all_albums():
    title = 'All Albums'
    description = 'The following table lists all the Albums currently in stock at Chinook.'
    query = queries.SELECT_ALL_ALBUMS
    return get_template(query, title, description)

@route('/select_album_tracks')
def select_album_tracks():
    title = 'All Albums (for tracks)'
    description = 'The following table lists all the Albums currently in stock at Chinook.'
    query = queries.SELECT_ALBUM_NAMES
    albums = run_query(query)
    return template('form_tracks_in_album', records=albums)

@route('/select_album_tracks', method='POST')
def select_album_tracks():
    album_value = request.forms.get('album_value')
    values = {'album_title': album_value }

    title = f'Tracks in {album_value}'
    description = f'This page shows the tracks in the album {album_value}'
    query = queries.SELECT_ALBUM_TRACKS
    return get_template_with_parameters(query, values, title, description)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Queries to find information about Customers
@route('/select_all_customers')
def select_all_albums():
    title = 'All Customers'
    description = 'The following table lists all the Customers that have placed orders at Chinook.'
    query = queries.SELECT_ALL_CUSTOMERS
    return get_template(query, title, description)

@route('/insert_new_customer', method='POST')
def insert_new_customer():
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    email = request.forms.get('email')
    form_data = dict(request.params)
    query = '''INSERT INTO Customer (FirstName, LastName, Email) VALUES (:first_name, :last_name, :email)'''
    result = run_insert_query(query, form_data)
    return f'''<h1>Customer inserted - {result}</h1>
                <p>{first_name} {last_name} {email}</p>
                <p>{form_data}</p>'''

@route('/remove_customer', method='POST')
def remove_customer():
    customer_id = request.forms.get('customer_id')
    values = { 'customer_id': customer_id }
    query = '''
                DELETE FROM Customer
                WHERE CustomerId = :customer_id
            '''
    result = run_insert_query(query, values)
    return f'''<h1>Customer {customer_id} removed</h1>'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Queries to find information about Orders
@route('/select_all_orders')
def select_all_albums():
    title = 'All Orders'
    description = 'The following table lists all the Orders that have been placed with Chinook.'
    query = queries.SELECT_ALL_ORDERS
    return get_template(query, title, description)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Static files
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

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

def run_insert_query(query, values):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(query, values)

        connection.commit()
        connection.close()

        return "success"
    
    except Exception as e:
        print("Error: ", e)
        connection.rollback()
        connection.close()
        return "error"

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
run(host='localhost', port=8081, debug=True, reloader=True)