import time

from data_filtering import *
from data_text_file_generation import *
from data_visualization import *

if __name__ == '__main__':
    start = time.time()

    database = "employees"
    table = "salaries"
    current_database = DatabaseTextFile(database, table, "localhost", "root",
                                        "Kom12345", "3306")
    # 87 sec
    #current_database.database_data_to_text("utf-8", 3000000)

    filtered_data = DataFiltering("salaries_data.txt", "utf-8")

    #filtered_data.isolate_entry("yearly_income.txt", 1)

    #filtered_data.filter_out_("Out_filtered_entries", "strings")

    visualize_data = DataVisualizer("yearly_income.txt", 100)
    #visualize_data.histogram_of_salaries()

    print(time.time()-start)

