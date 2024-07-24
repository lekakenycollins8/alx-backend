#!/usr/bin/env python3
"""Least Recently Used caching replacement policy"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU caching replacement policy"""
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.stack.remove(key)
            self.stack.append(key)
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed = self.stack.pop(0)
            del self.cache_data[removed]
            print("DISCARD: {}".format(removed))
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key, None)
