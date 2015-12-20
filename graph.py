#!/usr/bin/env python3


import json
import matplotlib.pyplot as plt
from sys import argv


def graph_db(dbFileUp, dbFileDown):
    dataUp = load_db(dbFileUp)
    dataDown = load_db(dbFileDown)
    timesUp, bwsUp = parse_data(dataUp)
    timesDown, bwsDown = parse_data(dataDown)
    plotUp, = plt.plot(timesUp, bwsUp)
    plotDown, =  plt.plot(timesDown, bwsDown)
    plt.legend([plotUp, plotDown], ['Up', 'Down'])
    plt.show()


def load_db(dbFile):
    db = open(dbFile, 'r')
    data = json.load(db)
    db.close()
    return data


def parse_data(data):
    bws = []
    times = []
    for result in data:
        times.append(result["start"]["timestamp"]["timesecs"])
        try:
            bws.append(result["end"]["sum_sent"]["bits_per_second"])
        except:
            bws.append(0)
    return times, bws

if __name__ == "__main__":
    graph_db(argv[1], argv[2])
