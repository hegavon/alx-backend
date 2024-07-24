#!/usr/bin/env python3
""" LFU caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = {}
        self.usage = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage.remove(key)
            self.usage.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = self.get_lfu_key()
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.usage.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
        return None

    def get_lfu_key(self):
        """ Get the least frequently used key """
        min_freq = min(self.frequency.values())
        lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
        if len(lfu_keys) == 1:
            return lfu_keys[0]
        else:
            for key in self.usage:
                if key in lfu_keys:
                    return key
