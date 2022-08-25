#!/usr/bin/python3
"""inherits from BaseCaching and is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """subclass FIFOCache"""

    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the
        key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for key, item in list(self.cache_data.items()):
                del self.cache_data[key]
                print("DISCARD: {}".format(key))
                break

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key not in self.cache_data or key is None:
            return (None)
        return (self.cache_data[key])
