import csv
import time

from rich.console import Console
from rich.table import Table

console = Console()
table = Table()

set_timer = time.time()

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

    capacity = max_price
    len_data = len(data)
    selected_elements = []

    while capacity >= 0 and len_data >= 0:
        last_element = data[len_data - 1]

        if matrix[len_data][capacity] == matrix[len_data - 1][capacity - last_element[1]] + last_element[2]:
            float_price = last_element[1] / 100
            float_profit = last_element[2] / 100
            selected_elements.append((last_element[0], float_price, float_profit))
            capacity -= last_element[1]  # remove capacity

        len_data -= 1

    profit = matrix[-1][-1] / 100
    return profit, selected_elements


def display_result(value):
    value[1].reverse()
    cost = []
    table.add_column("[#8e1b1b]Actions sélectionnées", justify="center", style="#588723")
    for i in range(len(value[1])):
        table.add_row(f"{value[1][i][0]}")
        cost.append(value[1][i][1])
    console.print(table, justify="center")
    console.print(f"[#aba6a6]Prix total des actions: [#8e1b1b]{sum(cost)} €[/]", justify="center")
    console.print(f"[#aba6a6]Bénéfice total des actions au bout de 2 ans: [#588723]{value[0]} €[/]",
                  justify="center")
    console.print(f"[#aba6a6]Temps écoulé: [#D2BFF0]{time.time() - set_timer} sec[/]", justify="center")


data = get_csv_data("data/dataset0.csv")
value = select_action(data, 50000)
display_result(value)
