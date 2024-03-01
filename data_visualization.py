import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self, data_file_name, bins=10):
        self.data_file_name = data_file_name
        self.bins = bins

    def histogram_of_salaries(self):
        try:
            with open(self.data_file_name, 'r') as file:
                # Convert each line to a floating-point number and store in a list
                salaries = []
                for line in file:
                    cleaned_line = line.strip()
                    salary = float(cleaned_line)

                    salaries.append(salary)

            # Create a histogram
            plt.hist(salaries, bins=self.bins, color='skyblue', edgecolor='black')

            # Add labels and title
            plt.xlabel('Salary')
            plt.ylabel('Frequency')
            plt.title('Histogram of Salaries')

            # Show the plot
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except FileNotFoundError:
            print(f"Error: File '{self.data_file_name}' not found.")
        except ValueError:
            print(f"Error: Unable to parse data in '{self.data_file_name}'")
        except Exception as e:
            print(f"Error: Unexpected error occurred: {e}")
