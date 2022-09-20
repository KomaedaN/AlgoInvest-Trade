import csv


def get_csv_data(url):
    """
    get_csv_data read and get csv data from a file

    :cost: cost data from csv file
    :benefit: benefit data from csv file
    :profit: calculate profit
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
    :return: profit result
    """
    return (cost * benefit) / 100


get_csv_data("data/dataset0.csv")
