import pandas

class Reader:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pandas.read_csv(filepath)
        self.dataframe = pandas.DataFrame(data=self.data)

        # get the math operation and rows of data as tuples
        self.operation = self.get_operation_name()
        self.rows = self._get_rows()

    def calculate_file(self):
        """
        read a file and perform required math calculation using filename
        return a 2d list with following format for each item - [expected_result, calculated_result]
            - expected_result, value we expect from calculation gotten from each line in the file
            - calculated_result, the value we calculate from the numbers in the file
        """
        # operation = reader.operation
        results = []

        for row in self.rows:
            expected_result = row[0]
            vals = row[1:]
            Calculator.calculate_numbers(operation, *vals)

            results.append([expected_result, *vals])

        return results

    def get_operation_name(self):
        """ extract the operation name from filepath to get operation type """
        filepath = self.filepath[:-4]  # remove .csv extension
        filepath = filepath.split("/")   # split the string into list using "/" as delimiter
        return filepath[-1]   # the filename should rest in the last position of the list

    def _get_rows(self):
        """
        returns a 2d list
        The first index of each internal list is the result/ expectant value
        every subsequent value is a number to be calculated
        """
        cols = list(self.dataframe.columns)

        rows = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(cols)):
                col = cols[j]
                row.append(self.dataframe[col][i])
            rows.append(row)

        return rows

