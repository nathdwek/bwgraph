#!/usr/bin/env python3

import json
from time import time
from sys import stdin, argv


def add_test(results, dbFile):
    try:
        db = open(dbFile, 'r')
        existingData = json.load(db)
        db.close()
    except FileNotFoundError:
        existingData = []
    existingData.append(results)
    db = open(dbFile, 'w')
    json.dump(existingData, db, indent=2)
    db.write('\n')
    db.close()


def load_test():
    result = json.load(stdin)
    if "timestamp" not in result["start"]:
        result["start"]["timestamp"] = {"timesecs": round(time())}
    return result

if __name__ == "__main__":
    add_test(load_test(), argv[1])
