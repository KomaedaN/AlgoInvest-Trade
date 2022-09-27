import csv
import time

from rich.console import Console
from rich.table import Table
from itertools import combinations

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
            cost = float(row[1])
            benefit = float(row[2])
            data_list.append((row[0], cost, benefit))
        return data_list


def select_action(data, max_price):
    """
    select_action try all combinations, compare max price and action cost, compare total benefit and benefit

    :data: action data
    :max_price: selected maximum price
    :return: return the most profitable actions compare to the maximum budget
    """
    benefit = 0.0
    action_list = []
    for i in range(len(data)):
        combination = combinations(data, i + 1)
        for list_data in combination:
            total_cost = calcul_cost(list_data)
            if total_cost <= max_price:
                total_benefit = benefit_value(list_data)
                if total_benefit > benefit:
                    action_list = list_data
                    benefit = total_benefit
    return action_list


def calcul_cost(data):
    cost = []
    for value in data:
        cost.append(value[1])
    return sum(cost)


def benefit_value(data):
    """Valeur en % de la combinaison courante

    @param stock_combination : liste des actions de la combinaison courante
    @return: sum profits (float) en %
    """
    profits = []
    for element in data:
        profits.append(element[1] * element[2] / 100)
    return sum(profits)


def display_result(list_data):
    table.add_column("[#8e1b1b]Actions sélectionnées", justify="center", style="#588723")
    for i in range(len(list_data)):
        table.add_row(f"{list_data[i][0]}")
    console.print(table, justify="center")
    console.print(f"[#aba6a6]Prix total des actions: [#8e1b1b]{calcul_cost(list_data)} €[/]", justify="center")
    console.print(f"[#aba6a6]Bénéfice total des actions au bout de 2 ans: [#588723]{benefit_value(list_data)} €[/]",
                  justify="center")
    console.print(f"[#aba6a6]Temps écoulé: [#D2BFF0]{time.time() - set_timer} sec[/]", justify="center")


data = get_csv_data("data/dataset0.csv")
list_data = select_action(data, 500.0)
display_result(list_data)
