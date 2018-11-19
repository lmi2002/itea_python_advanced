from flask import Flask
from flask import request
import collections
import csv

app = Flask(__name__)


@app.route("/add", methods=['POST'])
def index():
    if request.method == 'POST':
        csv_obj = Csv()
        csv_obj.writer_csv('g', 1)


class Csv:

    def __init__(self):
        self.dct = {}
        self.lst = []

    def writer_csv(self, *args):
        self.dct['product_name'] = args[0]
        self.dct['amount'] = args[1]

        with open('data.csv', 'a', newline='')as csvfile:
            fieldnames = ['product_name', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(self.dct)

    def reader_csv(self):
        with open('data.csv', newline='') as csvfile:
            fieldnames = ['product_name', 'amount']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                self.lst.append({'product_name': row['product_name'], 'amount': int(row['amount'])})
        print(self.lst)
