from app.controllers.controller import ControllerBase
from flask import render_template
from calculator.helpers.history import History
from calculator.helpers.csv_handler import Reader
from calculator.helpers.history import History


class HistoryController(ControllerBase):
    """ will retrieve all rows of history in data.csv """

    @staticmethod
    def post():
        History.clear_history()

        return render_template('history.html')


    @staticmethod
    def get():
        rows = Reader.get_rows("app/data.csv")

        print("in history controller", rows)

        # calculation_data = [
        #     ["addition", "10", "5 5"],
        #     ["addition", "20", "10 5 5"],
        #     ["subtraction", "25", "100 75"],
        #     ["multiplication", "1200", "5 8 3 5 2"],
        #     ["division", "7", "49 7"],
        # ]

        return render_template('history.html', rows=rows)
