#!/usr/bin/env python3


import json
import matplotlib.pyplot as plt
from sys import argv


def parse_db(dbFile):
    db = open(dbFile, 'r')
    data = json.load(db)
    db.close()
    bws = []
    times = []
    for result in data:
        times.append(result["start"]["timestamp"]["timesecs"])
        try:
            bws.append(result["end"]["sum_sent"]["bits_per_second"])
        except:
            bws.append(0)
    plt.plot(times, bws)
    plt.show()
    return times, bws


if __name__ == "__main__":
    print(parse_db(argv[1]))
