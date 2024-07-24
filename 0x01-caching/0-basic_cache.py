#!/usr/bin/env python3
""" Basic caching """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Store a key-value pair
        Args:
            key: the key to store
            item: the item to store
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to key
        If key is None or doesn't exist, return None
        """
        return self.cache_data.get(key, None)
