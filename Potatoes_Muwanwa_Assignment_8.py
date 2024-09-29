# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:41:16 2024

@author: tshik
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the directory and file name
directory = os.getcwd()  # This will set the current directory where the script is running from
file_name = 'FAOSTAT_data.csv'
file_path = os.path.join(directory, file_name)

try:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Display basic information about the CSV
    print("Basic Information about the dataset:")
    df.info()

    # Extract rows where 'Item' is 'Potatoes' and 'Element' is either 'Area harvested' or 'Yield'
    potatoes_data = df[(df['Item'] == 'Potatoes') & (df['Element'].isin(['Area harvested', 'Yield']))]

    # Select only the 'Year' and 'Value' columns
    potatoes_data = potatoes_data[['Year', 'Element', 'Value']]

    # Convert the result to a NumPy array
    potatoes_array = potatoes_data.pivot(index='Year', columns='Element', values='Value').reset_index().values

    # Separate years, area harvested, and yields into arrays
    years = potatoes_array[:, 0]  # Year column
    area_harvested = potatoes_array[:, 1]  # Area harvested column
    yields = potatoes_array[:, 2]  # Yield column

    # Display first few rows of the extracted data
    print("\nFirst 5 rows of the extracted data for 'Potatoes':")
    print(potatoes_data.head())

    # Identify the years with the maximum and minimum yield
    max_yield_year = years[np.argmax(yields)]
    min_yield_year = years[np.argmin(yields)]
    print("Year with Maximum Yield:", max_yield_year)
    print("Year with Minimum Yield:", min_yield_year)

    # Calculate mean yield
    mean_yield = np.mean(yields)
    print("Mean Yield:", mean_yield)

    # Calculate yield anomalies
    anom_yield = yields - mean_yield
    print("Yield Anomalies:", anom_yield)

    # Create a DataFrame for yield anomalies and save it to a CSV file
    anomalies_df = pd.DataFrame({'Year': years, 'Yield Anomaly': anom_yield})
    anomalies_df.to_csv('yield_anomalies.csv', index=False)
    print("Yield anomalies saved to 'yield_anomalies.csv'.")

    # Plot a time series of area harvested
    plt.figure(figsize=(12, 6))
    plt.plot(years, area_harvested, marker='o', linestyle='-', color='green')
    plt.xlabel('Year')
    plt.ylabel('Area Harvested (hectares)')
    plt.title('Area Harvested for Potatoes Over Time')
    plt.grid()
    plt.show()

    # Plot a time series of yield anomalies
    plt.figure(figsize=(12, 6))
    plt.bar(years, anom_yield, color='b', edgecolor='black')
    plt.xlabel('Year')
    plt.ylabel('Yield Anomaly (Deviation from Mean)')
    plt.title('Potato Yield Anomalies Over Time')
    plt.axhline(0, color='red', linestyle='--')  # Mean line
    plt.grid()
    plt.show()

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found in the directory '{directory}'.")

except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty or corrupted.")

except pd.errors.ParserError:
    print("Error: There was an error parsing the CSV file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
