import csv
from itertools import combinations


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
            profit = calcul_profit(cost, benefit)
            data_list.append((row[0], cost, benefit, profit))
        return data_list


def calcul_profit(cost, benefit):
    """
    :cost: cost per action
    :benefit: percentage of cost of action
    :return: profit result
    """
    return (cost * benefit) / 100


def sort_benefit(data_list):
    return sorted(data_list, key=lambda x: float(x[2]), reverse=True)


def choose_action(test):
    benefit = 0.0
    max_price = 500.0
    start = 0.0
    action_list = []
    for i in range(len(test)):

        datas = combinations(test, i + 1)
        for data in datas:
            if start + data[i][1] <= max_price:
                profit = profit_value(data)
                if profit > benefit:
                    start = data[i][1]
                    benefit = profit
                    action_list.append(data)
    print(action_list)
    print(start)
    print(benefit)

def profit_value(stock_combination):
    """Valeur en % de la combinaison courante

    @param stock_combination : liste des actions de la combinaison courante
    @return: sum profits (float) en %
    """
    profits = []
    for element in stock_combination:
        profits.append(element[1] * element[2] / 100)
    return sum(profits)
data = get_csv_data("data/dataset0.csv")
sorted_list = sort_benefit(data)
choose_action(data)
