#!/usr/bin/env python3

import json
import csv
from time import time
from sys import stdin, argv


def add_test(result, dbFile):
    if result:
        with open(dbFile, 'a', newline='') as db:
            writer = csv.writer(db, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([result["start"]["timestamp"]["timesecs"],
                            result["end"]["sum_sent"]["bits_per_second"],
                            result.get("error", "")])


def load_test():
    result = json.load(stdin)
    if "timestamp" not in result["start"]:
        result["start"]["timestamp"] = {"timesecs": round(time())}
    if "sum_sent" not in result["end"]:
        result["end"]["sum_sent"] = {"bits_per_second": 0}
    if result.get("error", "") == "error - the server is busy running a test. try again later":
        result = {}
    return result

if __name__ == "__main__":
    add_test(load_test(), argv[1])
