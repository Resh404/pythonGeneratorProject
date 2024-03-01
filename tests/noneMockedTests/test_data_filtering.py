import os
import pytest
from data_filtering import *


# Fixture to create a temporary test file
@pytest.fixture(scope="module")
def test_tmp_file():
    # Write test data to the file
    file = "test_tmp_file.txt"
    with open(file, "w") as f:
        f.write("1,John,Doe\n2,Alice,Smith\n3,Max,Pain\n")

    yield file

    os.remove("test_tmp_file.txt")
    os.remove("filtered_tmp_file.txt")
    os.remove("filtered_out_tmp_file.txt")


def test_my_read_line(test_tmp_file):
    # Create an instance of DataFiltering
    data_filtering = DataFiltering(collect_data_from=test_tmp_file, data_encoding="utf-8")

    # Call the method to read lines from the file
    lines = list(data_filtering.my_read_line())

    # Assert that the lines are read correctly
    assert lines == ["1,John,Doe\n", "2,Alice,Smith\n", "3,Max,Pain\n"]


def test_isolate_entry(test_tmp_file):
    # Create an instance of DataFiltering
    data_filtering = DataFiltering(collect_data_from=test_tmp_file, data_encoding="utf-8")

    # Call the method to isolate an entry
    file = "filtered_tmp_file.txt"
    data_filtering.isolate_entry(filtered_data_file_name=file, index=1)

    # Read the filtered file and assert its content
    with open(file, "r") as f:
        assert f.read() == "John\nAlice\nMax\n"


def test_filter_out_(test_tmp_file):
    # Create an instance of DataFiltering
    data_filtering = DataFiltering(collect_data_from=test_tmp_file, data_encoding="utf-8")

    # Call the method to filter out entries
    file = "filtered_out_tmp_file.txt"
    data_filtering.filter_out_(filtered_data_file_name=file, str_or_int_entries="string")

    # Read the filtered file and assert its content
    with open(file, "r") as f:
        assert f.read() == "1\n2\n3\n"
