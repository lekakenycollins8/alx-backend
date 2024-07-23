#!/usr/bin/env python3
"""Caching system that inherits from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """cashing system with no limit"""
    def put(self, key, item):
        """adds item to cached data"""
        if key or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """returns cached data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
