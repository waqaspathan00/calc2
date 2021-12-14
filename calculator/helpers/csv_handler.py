""" Contains Reader and Writer classes for parsing csv test files """

import time
import csv
import os
import pandas

class Reader:
    """ Use to get data rows and math operation from a CSV file """

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

        TODO: optimize and clean up the code using built in df methods
        """
        data = pandas.read_csv(filepath)
        dataframe = pandas.DataFrame(data=data)
        cols = list(dataframe.columns)

        rows = []
        for i in range(len(data)):
            row = []
            for j in range(len(cols)):  # pylint: disable=consider-using-enumerate
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


class Writer:  # pylint: disable=too-few-public-methods
    """ Writes log files containing data about the test that was completed """

    @staticmethod
    def write_line(infile, row):
        """
        Writes a log file containing data defined in _create_row()
        """

        with open(infile, "a") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    @staticmethod
    def write_division_log():
        """
        write a log file containing a row of data
            - record number
            - filename of the input file
        """
        record_num = len(os.listdir("tests/exceptions/"))
        filepath = "tests/exceptions/log_" + str(record_num) + ".txt"
        row = [record_num, filepath]

        with open(filepath, "w") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    @staticmethod
    def write_log(input_file):
        """
        Writes a log file containing data defined in _create_row()
        """

        filepath, row = Writer._create_row(input_file)

        with open(filepath, "w") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    @staticmethod
    def _create_row(input_file):
        """
        private method, create a row of data
            - unix time stamp
            - filename of the input file
            - record number
            - math operation
        """

        time_stamp = time.time()
        filename = Reader.get_operation_name(input_file) + ".csv"
        record_num = len(os.listdir("tests/completed/"))
        filepath = "tests/completed/log_" + str(record_num) + ".txt"
        operation = Reader.get_operation_name(input_file)
        row = [time_stamp, filename, record_num, operation]

        return filepath, row
