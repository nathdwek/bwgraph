import json
from time import time
from sys import stdin
import matplotlib.pyplot as plt
from sys import argv


def add_test(results, dbFile):
    try:
        db = open(dbFile, 'r')
        existingData = json.load(db)
        db.close()
    except FileNotFoundError:
        existingData = []
    existingData.append(results)
    db = open(dbFile, 'w')
    json.dump(existingData, db, indent = 2)
    db.write('\n')
    db.close()


def load_test():
    return json.load(stdin)


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
    print(times, bws)
    plt.plot(times, bws)
    plt.show()

if __name__ == "__main__":
    add_test(load_test(), argv[1])
