#!/usr/bin/python3
"""inherits from BaseCaching and is a caching system"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """subclass LIFOCache"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the
        key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for key, item in list(self.cache_data.items()):
                self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(list(self.cache_data.keys())[-1]))
                break

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key not in self.cache_data or key is None:
            return (None)
        self.cache_data.move_to_end(key)
        return (self.cache_data[key])
