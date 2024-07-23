#!/usr/bin/env python3
"""FIFO caching"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First in First Out caching replacement policy"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed = self.queue.pop(0)
            del self.cache_data[removed]
            print("DISCARD: {}".format(removed))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
