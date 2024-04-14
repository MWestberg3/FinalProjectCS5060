import pandas as pd
import matplotlib.pyplot as plt

def graph_employment(csv_file):

    # Load the CSV file into a DataFrame
    data = pd.read_csv(csv_file)

    # Flatten the data into a single column
    values = data.iloc[:, 1:].values.flatten()

    # Create a corresponding index for the flattened data
    years = data['Year'].values
    months = data.columns[1:]
    index = [f"{year}-{month}" for year in years for month in months]

    # Plot the data
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(index, values)

    # Add labels and title
    plt.xticks([])
    plt.xlabel("Time (Jan 2014 - Present)")
    plt.ylabel("All Employees, Thousands")
    plt.title("Employment in Tech (U.S.)")

    # Show plot
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

if __name__ == "__main__":
    print("==== GRAPHING EMPLOYMENT IN DATA PROCESSING, HOSTING, AND RELATED SERVICES ====")
    graph_employment("EuropeanCallOption/data/Tech_Industry_Employment.csv")

