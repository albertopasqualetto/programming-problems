#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
from collections import defaultdict
import random

class RandomizedSet:
    l = None

    def __init__(self):
        self.l = defaultdict(lambda: False)

    def insert(self, val: int) -> bool:
        out = not self.l[str(val)]
        self.l[str(val)] = True
        return out

    def remove(self, val: int) -> bool:
        out = self.l[str(val)]
        self.l.pop(str(val))
        return out

    def getRandom(self) -> int:
        return int(random.choice(list(self.l.keys())))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
