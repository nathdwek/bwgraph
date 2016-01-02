#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
from matplotlib.dates import epoch2num, DateFormatter
from sys import argv


def bwRead(db):
    bws = []
    times = []
    with open(db) as csvFile:
        reader = csv.DictReader(csvFile, delimiter=',')
        for row in reader:
            bws.append(float(row['bandwidth'])/1e6)
            times.append(epoch2num(int(row['epoch_time'])))
    return tuple(times), bws


def present(timesBwsDict):
    fig, ax = plt.subplots()
    for times in timesBwsDict:
        ax.plot_date(times, timesBwsDict[times], '-')
    plt.ylabel('Bandwidth [Mbit/s]')
    plt.xlabel('Time')
    # Choose your xtick format string
    date_fmt = '%d-%m-%y %H:%M'
    # Use a DateFormatter to set the data to the correct format.
    date_formatter = DateFormatter(date_fmt)
    ax.xaxis.set_major_formatter(date_formatter)
    # Sets the tick labels diagonal so they fit easier.
    fig.autofmt_xdate()

    plt.legend([argv[1], argv[2]])

if __name__ == "__main__":
    timesBwsDict = {}
    for i in (1, 2):
        times, bws = bwRead(argv[i])
        timesBwsDict[times] = bws
    present(timesBwsDict)
    if len(argv) >= 4:
        plt.savefig(argv[3])
    else:
        plt.show()
