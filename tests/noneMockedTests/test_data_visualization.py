import pytest
from data_visualization import *


# Fixture to create a test instance of DataVisualizer
@pytest.fixture
def data_visualizer(tmp_path) -> DataVisualizer:
    # Create a temporary file with test data
    data_file_path = tmp_path / "test_data.txt"
    with open(data_file_path, "w") as f:
        f.write("100\n200\n300\n400\n500\n")

    # Create an instance of DataVisualizer
    visualizer = DataVisualizer(data_file_name=data_file_path, bins=10)
    return visualizer


# Compare the images given by real function to the test function
@pytest.mark.mpl_image_compare
def test_histogram_of_salaries(data_visualizer):
    # Call the method being tested
    data_visualizer.histogram_of_salaries()
