from collections import deque
import copy
import requests
import math


class Lookback:

    def __init__(self, length=4):
        self.q = deque()
        for i in range(length):
            self.q.append(0)

    def _is_zeroqueue(self, data):
        localqueue = copy.deepcopy(data)
        while len(localqueue) > 0:
            if localqueue.popleft() > 0:
                return False
        return True

    def add_value(self, value):
        current = 0
        last = int(math.floor(value))
        self.q.append(last)
        first = self.q.popleft()

        if last == 0 and first > 0:
            if self._is_zeroqueue(self.q):
                requests.get("https://webhook")
                print "sent message"
        current += 1








