import csv


def get_csv_data(url):
    with open(url) as file_csv:
        reader = csv.reader(file_csv, delimiter=",")
        data_list = []
        for row in reader:
            cost = float(row[1])
            benefit = float(row[2])
            profit = (cost * benefit) / 100  # profit result
            data_list.append((row[0], cost, benefit, profit))
        return data_list


get_csv_data("data/dataset0.csv")
