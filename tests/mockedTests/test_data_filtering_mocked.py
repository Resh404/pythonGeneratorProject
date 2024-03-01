import pytest
from data_filtering import DataFiltering


# Fixture to create a test instance of DataFiltering
@pytest.fixture
def data_filtering_instance():
    return DataFiltering(collect_data_from="test_file.txt", data_encoding="utf-8")


def test_my_read_line_mocked(data_filtering_instance, mocker):
    # Mock "open" function to return a MagicMock object with predefined data
    mocker_open = mocker.mock_open(read_data="line1\nline2\nline3\n")
    mocker.patch("builtins.open", mocker_open)

    # Call the method being tested
    result = list(data_filtering_instance.my_read_line())

    # Assertions
    assert result == ["line1\n", "line2\n", "line3\n"]
    mocker_open.assert_called_once_with("test_file.txt", "r", encoding="utf-8")


def test_isolate_entry_mocked(data_filtering_instance, mocker):
    # Mock my_read_line method to return a predefined line
    mocker.patch.object(DataFiltering, 'my_read_line', return_value=["entry1,entry2,entry3\n"])

    # Mock "open" function to return a MagicMock object
    mocker_open = mocker.mock_open()
    mocker.patch("builtins.open", mocker_open)

    # Call isolate_entry method
    data_filtering_instance.isolate_entry("test_file.txt", 2)

    # Assert that "open" is called with the correct arguments
    mocker_open.assert_called_once_with("test_file.txt", "a", encoding="utf-8")

    # Assert that the write method of the file handle is called with the expected content
    mock_file_handle = mocker_open()
    mock_file_handle.write.assert_called_once_with("entry3\n")


def test_filter_out__mocked(data_filtering_instance, mocker):
    # Mock my_read_line method to return a predefined line
    mocker.patch.object(DataFiltering, 'my_read_line', return_value=["entry1,entry2,entry3\n"])

    # Mock "open" function to return a MagicMock object
    mocker_open = mocker.mock_open()
    mocker.patch("builtins.open", mocker_open)

    # Call filter_out_ method
    data_filtering_instance.filter_out_("test_file.txt", 0)

    # Assert that "open" is called with the correct arguments
    mocker_open.assert_called_once_with("test_file.txt", 'a', encoding="utf-8")

    # Assert that the write method of the file handle is called with the expected content
    mock_file_handle = mocker_open()
    mock_file_handle.write.assert_called_once_with("entry1,entry2,entry3\n")
