"""
Task A: Better structure
I decided to separate the main function into 3 smaller and more focused functions.
The functions are:
    - read_data
    - calculate_average
    - print_results

The main function is now much more readable and the code is easier to understand.
Each function has a docstring that explains what the function does and what it returns.
The variables are more descriptive and follow the PEP8 naming convention (i.e. snake_case)
using lowercase with underscores between words.


Task B: Error handling
I added error handling to the read_data function:
    - If the file is not found, the program will print an error message and ask the user to try again.
    - If a line in the file cannot be interpreted, the program will print a warning message and ignore that line.
This way, the program will not crash if the file is not formatted correctly.
I also modify the calculate_average function. If the batch does not contain any
valid measurements, the program will not add that batch to the processed_data dictionary.
"""
import matplotlib.pyplot as plt


def read_data(filename):
    """
    This function reads the data from a file and returns a dictionary.
    :param filename: The name of the file to be read.
    :return: A dictionary where the keys are batch names and the values are
    lists of tuples with x_coord, y_coord, and measurement values.
    """
    data = {}
    try:
        with open(filename, 'r') as file_handle:
            for line in file_handle:
                try:
                    batch, x_coord, y_coord, measurement = line.split(',')
                    if batch not in data:
                        data[batch] = []
                    data[batch].append((float(x_coord), float(y_coord), float(measurement)))
                except ValueError:
                    print(f"WARNING: Cannot interpret line: {line}. Ignoring this line.")
    except FileNotFoundError:
        print(f"ERROR: File {filename} not found. Please check the file name and try again.")
    return data


def calculate_average(data):
    """
    This function calculates the average of the values for each batch.
    :param data: A dictionary where the keys are batch names and the values
    are lists of tuples with x_coord, y_coord, and measurement values.
    :return: A dictionary where the keys are batch names and the values are
    the average of the values for that batch.
    """
    processed_data = {}
    for batch, sample in data.items():
        n_values = 0
        sum_values = 0
        for x_coord, y_coord, measurement in sample:
            if x_coord**2 + y_coord**2 <= 1:
                sum_values += measurement
                n_values += 1
        if n_values > 0:
            average = sum_values / n_values
            processed_data[batch] = average
    return dict(sorted(processed_data.items()))


def print_results(processed_data):
    """
    This function prints the processed data.
    :param processed_data: A dictionary where the keys are batch names and
    the values are the average of the values for that batch.
    """
    print("Batch\t Average")
    for batch, average in processed_data.items():
        print(batch, "  \t", average)


def plot_data(data, filename):
    """
    This function plots the data and saves the plot as a PDF file. The annotations for the scatter plot were taken from:
    https://stackoverflow.com/questions/14432557/scatter-plot-with-different-text-at-each-data-point
    :param data: A dictionary where the keys are batch names and the values
    are lists of tuples with x_coord, y_coord, and measurement values.
    :param filename: The name of the file to save the plot as.
    """
    # scatter plot for x and y coordinates
    fig, ax = plt.subplots()
    for batch, samples in data.items():
        x_coords = [sample[0] for sample in samples]
        y_coords = [sample[1] for sample in samples]
        measurement = [sample[2] for sample in samples]
        ax.scatter(x_coords, y_coords)
        for i, txt in enumerate(measurement):
            ax.annotate(txt, (x_coords[i], y_coords[i]))

    # plot circle
    circle = plt.Circle((0, 0), 1, color='black', fill=False)
    plt.gca().add_artist(circle)

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.savefig(f"{filename.split('.')[0]}.pdf")


def main():
    """
    This is the main body of the program. It prompts the user for the
    file name, reads the data, processes the data, and prints the results.
    """
    while True:
        filename = input('Which csv file should be analyzed? ')
        data = read_data(filename)
        if data:
            processed_data = calculate_average(data)
            print_results(processed_data)
            plot_data(data, filename)
            print(f"Plot saved as {filename.split('.')[0]}.pdf")
            break


# Start the main program
if __name__ == "__main__":
    main()
