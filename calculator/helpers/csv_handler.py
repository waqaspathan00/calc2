import pandas
import time
import csv
import os

class Reader:

    @staticmethod
    def process_file(filepath):
        """
        get the rows of a csv file and the operation name from filepath
        """
        rows = Reader.get_rows(filepath)
        operation = Reader.get_operation_name(filepath)

        return rows, operation

    @staticmethod
    def get_rows(filepath):
        """
        returns a 2d list
        The first index of each internal list is the result/ expectant value
        every subsequent value is a number to be calculated
        """
        filepath = filepath
        data = pandas.read_csv(filepath)
        dataframe = pandas.DataFrame(data=data)
        cols = list(dataframe.columns)

        rows = []
        for i in range(len(data)):
            row = []
            for j in range(len(cols)):
                col = cols[j]
                row.append(dataframe[col][i])
            rows.append(row)

        return rows

    @staticmethod
    def get_operation_name(filepath):
        """ extract the operation name from filepath to get operation type """
        filepath = filepath[:-4]  # remove .csv extension
        filepath = filepath.split("/")   # split the string into list using "/" as delimiter
        filepath = filepath[-1]  # the filename should rest in the last position of the list

        # remove the word "large" from the name if large data file
        if "large_" in filepath:
            filepath = filepath[6:]

        return filepath


class Writer:

    @staticmethod
    def write_log(input_file):
        """
        Writes a log file containing:
            - unix time stamp
            - filename of the input file
            - record number
            - operation
            - result of the calculation
        """

        ind = len(os.listdir("calculator/results/"))
        filename = "calculator/results/log_" + str(ind) + ".txt"
        operation = Reader.get_operation_name(input_file)
        row = [time.time(), input_file, ind, operation]

        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(row)
