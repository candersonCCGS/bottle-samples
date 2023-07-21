import sqlite3

###############################
# SET UP EMPTY DATABASE
#
# Drop the tables from the database if they exist so we can run the CREATE statements
# NOTE: If there is data in the database, tables need to be dropped in the correct order 
# to maintain referential integrity
#
def drop_tables(cursor):
    print('Drop tables if they exist')
    query = """
            DROP TABLE IF EXISTS Price;
            DROP TABLE IF EXISTS Station;
            DROP TABLE IF EXISTS Area;
            DROP TABLE IF EXISTS Product;
            DROP TABLE IF EXISTS Region;
            DROP TABLE IF EXISTS Brand;
            """
    # Use executescript as there are multiple queries in the same string
    cursor.executescript(query)

def update_pragma(cursor):
    # Update the database to allow foreign keys to enforce referential integrity
    print("Update PRAGMA to support foreign keys")
    query = "PRAGMA foreign_keys = ON"
    cursor.execute(query)

###############################
# CREATE EMPTY TABLES
#
# Create each individual table in the database.
# NOTE: Tables need to be created in correct order to ensure foreign key constraints will work
#
def create_region_table(cursor):
    print("Create Region Table")
    query = """CREATE TABLE Region (
        region_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )"""
    cursor.execute(query)

def create_area_table(cursor):
    print("Create Area Table")
    query = """CREATE TABLE Area (
        area_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        region_id INTEGER NOT NULL,
        FOREIGN KEY(region_id) REFERENCES Region(region_id)
        )"""
    cursor.execute(query)

def create_brand_table(cursor):
    print("Create Brand Table")
    query = """CREATE TABLE Brand (
        brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )"""
    cursor.execute(query)

def create_product_table(cursor):
    print("Create Product Table")
    query = """CREATE TABLE Product (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL,
        description TEXT NOT NULL
        )"""
    cursor.execute(query)

def create_station_table(cursor):
    print("Create Station Table")
    query = """CREATE TABLE Station (
        station_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT,
        city TEXT,
        postcode TEXT,
        brand_id INTEGER NOT NULL,
        area_id INTEGER NOT NULL,
        FOREIGN KEY(brand_id) REFERENCES Brand(brand_id),
        FOREIGN KEY(area_id) REFERENCES Area(area_id)
        )"""
    cursor.execute(query)

def create_price_table(cursor):
    print("Create Price Table")
    query = """CREATE TABLE Price (
        price_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        price INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        station_id INTEGER NOT NULL,
        FOREIGN KEY(product_id) REFERENCES Product(product_id),
        FOREIGN KEY(station_id) REFERENCES Station(station_id)
        )"""
    cursor.execute(query)

###############################
# CREATE DATABASE
#
# Create the database and populate it with empty tables
# Commit changes to the database so they are saved to the database and close connection.
# Any changes that are made prior to a commit will not be saved until they are committed.
#
def create_db(database_name):
    try:
        # Create connection to database
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        
        drop_tables(cursor)
        update_pragma(cursor)

        create_region_table(cursor)
        create_area_table(cursor)
        create_brand_table(cursor)
        create_product_table(cursor)
        create_station_table(cursor)
        create_price_table(cursor)
        
        # commit changes to the database so they are saved to the database and close connection
        connection.commit()
        connection.close()
        
        return "success"
    
    except Exception as e:
        print("Error: ", e)
        connection.rollback()
        connection.close()
        return "error"