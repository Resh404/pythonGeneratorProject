class DataFiltering:
    def __init__(self, collect_data_from: str, data_encoding: str):
        self.target_file_name = collect_data_from
        self.data_encoding = data_encoding

    def my_read_line(self):
        try:
            with open(self.target_file_name, "r", encoding=self.data_encoding) as file:
                for line in file:
                    yield line
        except FileNotFoundError:
            print(f"Error: File '{self.target_file_name}' not found.")
        except PermissionError:
            print(f"Error: Permission denied while trying to access file '{self.target_file_name}'.")
        except UnicodeDecodeError:
            print(f"Error: Unable to decode file '{self.target_file_name}' using encoding '{self.data_encoding}'.")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

    def isolate_entry(self, filtered_data_file_name: str, index: int):
        try:
            with open(filtered_data_file_name, "a", encoding=self.data_encoding) as output_file:
                for line in self.my_read_line():
                    line_entries = line.strip().split(',')
                    entry = line_entries[index]
                    output_file.write(entry + "\n")
        except Exception as e:
            print(f"Error: An unexpected error occurred while writing to file: {e}")

    def filter_out_(self, filtered_data_file_name: str, str_or_int_entries):
        try:
            with open(filtered_data_file_name, "a", encoding=self.data_encoding) as output_file:
                for line in self.my_read_line():
                    line_entries = line.strip().split(',')
                    int_line = []
                    str_line = []

                    for entry in line_entries:
                        if '-' in entry:
                            int_line.append(entry)
                        else:
                            try:
                                int(entry)
                                int_line.append(entry)
                                continue
                            except ValueError:
                                str_line.append(entry)

                    if isinstance(str_or_int_entries, str):
                        output_file.write(",".join(int_line) + "\n")
                    else:
                        output_file.write(",".join(str_line) + "\n")
        except Exception as e:
            print(f"Error: An unexpected error occurred while writing to file: {e}")
