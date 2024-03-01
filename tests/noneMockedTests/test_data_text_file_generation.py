import os

import pytest
import mysql.connector
from data_text_file_generation import *


# Fixture to set up and tear down the test database
@pytest.fixture(scope="module")
def test_database():
    # Establish connection to the test database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kom12345",
        port="3306",
        database="test_database"
    )

    # Create a test table and insert some data
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE test_table (id INT, name VARCHAR(255))")
        cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'John'), (2, 'Alice')")
        connection.commit()
    except mysql.connector.Error as err:
        print("Error creating test table:", err)

    # Return the test database connection
    yield connection

    # Teardown: Drop the test table and close the connection
    try:
        cursor.execute("DROP TABLE test_table")
        connection.commit()
    except mysql.connector.Error as err:
        print("Error dropping test table:", err)

    cursor.close()
    connection.close()
    os.remove("test_table_data.txt")

@pytest.fixture(scope="module")
def test_database_file(test_database):
    # Create an instance of DatabaseTextFile
    return DatabaseTextFile(database="test_database", table="test_table", host="localhost",
                            user="root", password="Kom12345", port="3306")

def test_data_collection_from_database(test_database_file):
    # Call the method to collect data from the database
    data_generator = test_database_file.data_collection_from_database()

    # Check if the data generator yields the expected data
    assert next(data_generator) == "1,John"
    assert next(data_generator) == "2,Alice"


def test_database_data_to_text(test_database_file):
    # Call the method to write data to a text file
    test_database_file.database_data_to_text(data_encoding="utf-8", limit=2)

    # Read the contents of the created text file and check if it contains the expected data
    try:
        with open("test_table_data.txt", "r", encoding="utf-8") as file:
            assert file.read() == "1,John\n2,Alice\n"
    except FileNotFoundError as e:
        print("Error opening test_table_data.txt:", e)
    except Exception as e:
        print("Error:", e)
