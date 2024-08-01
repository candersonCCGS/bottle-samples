from bottle import route, run, template, request, static_file
import sqlite3

##################################################
#
# Routes for each page
#
# Home page
@route('/')
def index():
    return template('index')

# Create new To Do list (remove existing list and create new empty table)
@route('/create_todo_list')
def create_todo_list():
    connection = sqlite3.connect('todo_list.sqlite')
    cursor = connection.cursor()

    query = 'DROP TABLE IF EXISTS Task'
    cursor.execute(query)

    query = '''
            CREATE TABLE Task
                (task_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT FALSE)
            '''
    cursor.execute(query)

    connection.commit()
    connection.close()

    return template('index')

# Insert some sample data to set up the to do list
@route('/insert_sample_data')
def insert_sample_data():
    connection = sqlite3.connect('todo_list.sqlite')
    cursor = connection.cursor()

    task1 = { 'title' : 'Wash car',
                'description': 'Take care to car wash and clean the outside',
                'completed' : False }
    task2 = { 'title' : 'Maths',
                'description' : 'Complete exercise 6 on page 231',
                'completed' : True }
    task3 = { 'title' : 'Shopping',
                'description' : 'Buy ingredients to cook spaghetti bolognese for dinner',
                 'completed' : False }
    
    query = 'INSERT INTO Task (title, description, completed) VALUES (:title, :description, :completed)'
    cursor.execute(query, task1)
    cursor.execute(query, task2)
    cursor.execute(query, task3)

    connection.commit()
    connection.close()

    return template('index')

# Retrieve all the items in the to do list and display them on the page
@route('/show_to_do_list')
def show_to_do_list():
    connection = sqlite3.connect('todo_list.sqlite')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    query = 'SELECT * FROM Task'
    cursor.execute(query)
    tasks = cursor.fetchall()
    
    connection.close()

    return template('index', records=tasks)

# Add new task
@route('/add_task', method='POST')
def add_task():
    connection = sqlite3.connect('todo_list.sqlite')
    cursor = connection.cursor()

    # Retrieve the values from the form as a dictionary
    # NOTE: HTML form field names (from the template) must match parameter names in INSERT query
    form_data = dict(request.params)
    query = 'INSERT INTO Task (title, description) VALUES (:title, :description)'
    cursor.execute(query, form_data)

    connection.commit()
    connection.close()

    return template('index')

# Mark task as completed
@route('/complete_task', method='POST')
def complete_task():
    connection = sqlite3.connect('todo_list.sqlite')
    cursor = connection.cursor()

    task_id = request.forms.get('task_id')
    values = { 'task_id' : task_id }
    query = '''
            UPDATE Task 
            SET completed = TRUE
            WHERE task_id = :task_id
            '''
    cursor.execute(query, values)

    connection.commit()
    connection.close()

    return template('index')

# Add new task
@route('/remove_task', method='POST')
def remove_task():
    connection = sqlite3.connect('todo_list.sqlite')
    cursor = connection.cursor()

    task_id = request.forms.get('task_id')
    values = { 'task_id' : task_id }
    query = 'DELETE FROM Task WHERE task_id = :task_id'
    cursor.execute(query, values)

    connection.commit()
    connection.close()

    return template('index')

# Static files
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

##################################################
#
# Helper functions

##################################################
#
# Run the web server to serve up the pages
#
run(host='localhost', port=8081, debug=True, reloader=True)