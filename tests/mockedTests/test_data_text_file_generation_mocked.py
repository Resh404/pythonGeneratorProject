import pytest
from data_text_file_generation import *


# Fixture to create a test instance of DatabaseTextFile
@pytest.fixture
def test_database(mocker):
    return DatabaseTextFile(database="test_db", table="test_table", host="localhost", user="user", password="password",
                            port="3306")


def test_data_collection_from_database(test_database, mocker):
    # Mock the connect method
    mock_connect = mocker.patch("mysql.connector.connect")

    # Mock the cursor and its methods
    mock_cursor = mock_connect.return_value.cursor.return_value
    mock_cursor.execute.return_value = None
    mock_cursor.fetchmany.side_effect = [[(1, "John", 6000)], []]

    # Execute the method and check the result
    result = list(test_database.data_collection_from_database())
    assert result == ["1,John,6000"]


def test_database_data_to_text(test_database, mocker):
    # Mock the data_collection_from_database method to return predefined data
    test_database.data_collection_from_database = mocker.MagicMock(return_value=["1,John,6000"])

    # Mock the open function to return a MagicMock object
    mock_open = mocker.mock_open()
    mocker.patch("builtins.open", mock_open)

    # Call the method and assert that the file is written correctly
    test_database.database_data_to_text(data_encoding="utf-8", limit=1)
    mock_open.assert_called_once_with("test_table_data.txt", 'w', encoding="utf-8")

    mock_file_handle = mock_open()
    mock_file_handle.write.assert_called_once_with("1,John,6000\n")
