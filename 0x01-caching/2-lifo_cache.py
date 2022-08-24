#!/usr/bin/python3
"""inherits from BaseCaching and is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """subclass LIFOCache"""

    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the
        key key"""
        if key or item in self.cache_data is None:
            pass
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.popitem()
            print("DISCARD: {}".format(list(self.cache_data.keys())[-1]))

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key not in self.cache_data or key is None:
            return (None)
        return (self.cache_data[key])
