import csv
from rich.console import Console
from rich.table import Table


def get_csv_data(url):
    """
    get_csv_data read and get csv data from a file

    :url: csv file link
    :return: return all data inside a list
    """
    with open(url) as file_csv:
        reader = csv.reader(file_csv, delimiter=",")
        data_list = []

        for row in reader:
            try:
                float(row[1])
                cost = float(row[1])
                benefit = float(row[2])
                data_list.append((row[0], cost, benefit))
            except ValueError:
                pass

        return data_list


def select_action(data, max_price):
    current_price = 0.0
    benefit = 0.0
    action_list = []


data = get_csv_data("data/dataset1.csv")
select_action(data, 500.0)
