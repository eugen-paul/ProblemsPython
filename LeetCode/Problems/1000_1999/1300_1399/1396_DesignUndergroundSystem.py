from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class UndergroundSystem:

    # CardId to (CheckInStation, CheckInTime)
    m: Dict[int, Tuple[str, int]]

    # (CheckInStation, CheckOutStation) to (sum all times, count)
    at: Dict[Tuple[str, str], Tuple[int, int]]

    def __init__(self):
        self.m = dict()
        self.at = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.m[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_in, time_in = self.m.pop(id)

        if (station_in, stationName) not in self.at:
            self.at[(station_in, stationName)] = (t-time_in, 1)
        else:
            data = self.at[(station_in, stationName)]
            self.at[(station_in, stationName)] = (data[0] + t-time_in, data[1]+1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        data = self.at[(startStation, endStation)]
        return data[0] / data[1]


def do_test(t: int, s, n, r):
    o: UndergroundSystem
    for i, c in enumerate(s):
        if c == "UndergroundSystem":
            o = UndergroundSystem()
        elif c == "checkIn":
            o.checkIn(n[i][0], n[i][1], n[i][2])
        elif c == "checkOut":
            o.checkOut(n[i][0], n[i][1], n[i][2])
        else:
            resp = round(o.getAverageTime(n[i][0], n[i][1]), 5)
            if r[i] != resp:
                print(t, "Error: Expects ", r[i], ", get ", resp)


if __name__ == "__main__":
    do_test(0,
            ["UndergroundSystem", "checkIn", "checkIn", "checkIn", "checkOut", "checkOut", "checkOut",
                "getAverageTime", "getAverageTime", "checkIn", "getAverageTime", "checkOut", "getAverageTime"],
            [[], [45, "Leyton", 3], [32, "Paradise", 8], [27, "Leyton", 10], [45, "Waterloo", 15], [27, "Waterloo", 20], [32, "Cambridge", 22], [
                "Paradise", "Cambridge"], ["Leyton", "Waterloo"], [10, "Leyton", 24], ["Leyton", "Waterloo"], [10, "Waterloo", 38], ["Leyton", "Waterloo"]],
            [None, None, None, None, None, None, None, 14.00000, 11.00000, None, 11.00000, None, 12.00000]
            )
    do_test(1,
            ["UndergroundSystem", "checkIn", "checkOut", "getAverageTime", "checkIn",
                "checkOut", "getAverageTime", "checkIn", "checkOut", "getAverageTime"],
            [[], [10, "Leyton", 3], [10, "Paradise", 8], ["Leyton", "Paradise"], [5, "Leyton", 10], [5, "Paradise", 16],
                ["Leyton", "Paradise"], [2, "Leyton", 21], [2, "Paradise", 30], ["Leyton", "Paradise"]],
            [None, None, None, 5.00000, None, None, 5.50000, None, None, 6.66667]
            )
