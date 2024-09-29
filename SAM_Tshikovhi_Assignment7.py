# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:29:06 2024

@author: tshik
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# Define the directory and updated file name
directory = r'C:\Users\tshik\OneDrive\Desktop\NQF 9\CCSC7900\handling text\handling text'
file_name = 'SAM.txt'  # Updated file name
file_path = os.path.join(directory, file_name)

# Check if the file exists
if os.path.exists(file_path):
    # Opening the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize a list to store SAM data and years
    sam_data = []
    years = []

    # Print raw data for debugging
    print("Raw Data Read from File:")
    for line in lines:
        print(repr(line.strip()))  # Use repr to see whitespace issues

    # Parse and extract data
    for line in lines:
        # Skip lines that are comments or headers
        if line.startswith('#') or len(line.strip()) == 0:
            continue

        # Split the line into individual elements
        data = line.split()

        # Print the split data for debugging
        print("Split Data:", data)

        # Ensure the line contains year + 12 months of data
        if len(data) == 13:
            try:
                year = int(data[0])  # Extract the year (first element)

                # Handle missing values represented by -999.9000
                monthly_values = []
                for value in data[1:]:
                    try:
                        num_value = float(value)
                        if num_value != -999.9000:  # Ignore missing values
                            monthly_values.append(num_value)
                    except ValueError:
                        print(f"Warning: Could not convert '{value}' to float.")

                # Print the parsed monthly values for debugging
                print("Parsed Monthly Values:", monthly_values)

                # Append the year and monthly values to their respective lists
                if len(monthly_values) == 12:  # Only append if all months have valid data
                    years.append(year)
                    sam_data.append(monthly_values)
                else:
                    print(f"Warning: Line does not have 12 valid monthly values: {line.strip()}")
            except ValueError:
                # Handle cases where data cannot be converted
                print(f"Skipping line due to conversion error: {line.strip()}")

    # Print the final SAM data for debugging
    print("Final SAM Data:", sam_data)

    # Convert the list of SAM data to a NumPy array
    sam_array = np.array(sam_data)
    years_array = np.array(years)

    # Check if sam_array is empty before proceeding
    if sam_array.size == 0:
        print("Error: No valid data was read from the file.")
    else:
        # 1. Calculate the average SAM value for each month across all years
        monthly_averages = np.mean(sam_array, axis=0)
        print("Monthly Averages (January to December):", monthly_averages)

        # 2. Calculate the standard deviation for each month
        monthly_std = np.std(sam_array, axis=0)
        print("Monthly Standard Deviations (January to December):", monthly_std)

        # 3. Identify the years with the maximum and minimum SAM value for each month
        max_years = np.argmax(sam_array, axis=0)
        min_years = np.argmin(sam_array, axis=0)

        for month in range(12):
            print(f"Month {month + 1}: Max year = {years_array[max_years[month]]}, Min year = {years_array[min_years[month]]}")

        # 4. Calculate the average SAM value for each year
        yearly_averages = np.mean(sam_array, axis=1)
        print("Yearly Averages:", yearly_averages)

        # 5. Write the monthly averages and standard deviations to an output file
        output_file_path = os.path.join(directory, 'SAM_monthly_stats.txt')
        with open(output_file_path, 'w') as output_file:
            output_file.write('Month\tAverage\tStandard Deviation\n')
            for month in range(12):
                output_file.write(f"{month + 1}\t{monthly_averages[month]:.2f}\t{monthly_std[month]:.2f}\n")
        print(f"Monthly averages and standard deviations written to {output_file_path}")

        # 6. Plot a time series of the monthly index values
        plt.figure(figsize=(12, 6))
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for month in range(12):
            plt.plot(years_array, sam_array[:, month], marker='o', label=months[month])
        plt.title('Time Series of Monthly SAM Values')
        plt.xlabel('Year')
        plt.ylabel('SAM Value')
        plt.legend(title='Months')
        plt.grid(True)
        plt.show()

        # 7. Plot the monthly mean SAM values (calculated in step 1)
        plt.figure(figsize=(10, 5))
        plt.plot(months, monthly_averages, marker='o', linestyle='-', color='g')
        plt.title('Average SAM Values for Each Month (All Years)')
        plt.xlabel('Month')
        plt.ylabel('Average SAM Value')
        plt.grid(True)
        plt.show()

        # 8. Plot the annual mean SAM values (calculated in step 4)
        plt.figure(figsize=(10, 5))
        plt.plot(years_array, yearly_averages, marker='o', linestyle='-', color='b')
        plt.title('Yearly Average SAM Values')
        plt.xlabel('Year')
        plt.ylabel('Average SAM Value')
        plt.grid(True)
        plt.show()

else:
    print(f"File '{file_name}' does not exist in the directory.")
