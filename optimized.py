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
                cost = int(float(row[1]) * 100)
                profit = float(row[2]) * cost / 100
                data_list.append((row[0], cost, profit))
            except ValueError:
                pass

        return data_list


def select_action(data, max_price):
    matrix = [[0 for x in range(max_price + 1)] for x in range(len(data) + 1)]  # init matrix

    for i in range(1, len(data) + 1):

        for w in range(1, max_price + 1):
            current_cost = data[i - 1][1]
            current_profit = data[i - 1][2]
            if current_cost <= w:
                matrix[i][w] = max(current_profit + matrix[i - 1][w - current_cost], matrix[i - 1][w])
            else:
                matrix[i][w] = matrix[i - 1][w]  # keep the previous data


data = get_csv_data("data/dataset0.csv")
select_action(data, 50000)
