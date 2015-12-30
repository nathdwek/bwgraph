#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
from matplotlib.dates import epoch2num, DateFormatter
from sys import argv


def plotBW(db, ax):
    bws = []
    times = []
    with open(db) as csvFile:
        reader = csv.DictReader(csvFile, delimiter=',')
        for row in reader:
            bws.append(float(row['bandwidth'])/1e6)
            times.append(epoch2num(int(row['epoch_time'])))
    ax.plot_date(times, bws, '-')

if __name__ == "__main__":
    fig, ax = plt.subplots()
    db1 = argv[1]
    db2 = argv[2]
    plotBW(db1, ax)
    plotBW(db2, ax)
    plt.ylabel('Bandwidth [Mbit/s]')
    plt.xlabel('Time')
    # Choose your xtick format string
    date_fmt = '%d-%m-%y %H:%M'

    # Use a DateFormatter to set the data to the correct format.
    date_formatter = DateFormatter(date_fmt)
    ax.xaxis.set_major_formatter(date_formatter)

    # Sets the tick labels diagonal so they fit easier.
    fig.autofmt_xdate()
    plt.legend([db1, db2])

    plt.show()
