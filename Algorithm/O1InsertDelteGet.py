import random


class RandomizedSet(object):
    # https://leetcode.cn/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
    def __init__(self):
        self.sets = set()

    def insert(self, val):
        if val in self.sets:
            return False
        self.sets.add(val)
        return True

    def remove(self, val):
        if val in self.sets:
            self.sets.discard(val)
            return True
        return False

    def getRandom(self):
        return random.choice(list(self.sets))
