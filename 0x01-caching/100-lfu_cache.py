#!/usr/bin/python3
"""inherits from BaseCaching and is a caching system"""
import collections
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """subclass LIFOCache"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data_frq = collections.defaultdict(collections.OrderedDict)
        self.least_freq = 1

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the
        key key"""
        if key is not None and item is not None:
            pass
        if key in self.cache_data:
            self._update(key, item)
        else:
            self.cache_data[key] = item
            self.cache_data_frq[1][key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for key, item in self.cache_data.items():
                    print("DISCARD: {}".format(key))
                    break
                rem = self.cache_data_frq[self.least_freq].popitem(last=False)
                self.cache_data.pop(rem[0])

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key not in self.cache_data or key is None:
            return (None)
        item = self.cache_data[key][0]
        self._update(key, item)
        return (item)

    def _update(self, key, item):
        """update dictionary"""
        freq = self.cache_data[key]
        """self.cache_data_frq[freq].pop(key)"""
        if len(self.cache_data_frq[self.least_freq]) == 0:
            self.least_freq += 1
        """self.cache_data_frq[freq+1][key] = item"""
        self.cache_data[key] = item
