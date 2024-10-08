#!/usr/bin/env python3
""" LIFO caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key is not None and self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
