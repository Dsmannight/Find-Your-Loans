# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, info):
    """Uses or creates a csv file to save information from user.

    Args:
        csvpath (path): The csv file path
        info: The information being written to csv

    Returns:

    """
    with open(csvpath, 'w') as file:
        writer = csv.writer(file)
        for line in info:
            writer.writerow(line)

