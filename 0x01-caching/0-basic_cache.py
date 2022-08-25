#!/usr/bin/python3
"""Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """initialize """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value
        for the key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key not in self.cache_data:
            return (None)
        return (self.cache_data[key])
