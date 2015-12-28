#!/usr/bin/env python3

import csv
from sys import argv

def init(dbFile):
    with open(dbFile, 'w', newline='') as db:
        fieldnames = ['epoch time', 'bandwidth', 'error']
        writer = csv.DictWriter(db, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()


if __name__ == '__main__':
    init(argv[1])
