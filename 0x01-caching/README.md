0x01-caching
This project involves implementing various caching systems using Python, following specific requirements and constraints. Each caching system is implemented as a class that inherits from a base class BaseCaching. Below are the details of each task and the implemented classes:

Requirements
Python scripts will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
All files should end with a new line.
The first line of all files should be exactly #!/usr/bin/env python3.
A README.md file, at the root of the project folder, is mandatory.
Code should use the pycodestyle style (version 2.5).
All files must be executable.
The length of files will be tested using wc.
All modules should have documentation.
All classes should have documentation.
All functions (inside and outside a class) should have documentation.
Documentation should be a real sentence explaining the purpose of the module, class, or method.
BaseCaching
The base class BaseCaching defines the structure and common functionality for all caching systems. It includes:

A constant MAX_ITEMS set to 4.
An initializer to create an empty dictionary cache_data to store cache items.
A method print_cache() to print the current state of the cache.
Abstract methods put(key, item) and get(key) that must be implemented by the subclasses.
Tasks
0. Basic dictionary
Create a class BasicCache that inherits from BaseCaching and implements a basic caching system with no limit.

put(self, key, item): Adds the item to the cache dictionary. If key or item is None, does nothing.
get(self, key): Returns the value associated with key in the cache dictionary. If key is None or does not exist, returns None.
1. FIFO Caching
Create a class FIFOCache that inherits from BaseCaching and implements a FIFO (First In, First Out) caching system.

put(self, key, item): Adds the item to the cache dictionary. If key or item is None, does nothing. If the cache exceeds MAX_ITEMS, the first item added is discarded.
get(self, key): Returns the value associated with key in the cache dictionary. If key is None or does not exist, returns None.
2. LIFO Caching
Create a class LIFOCache that inherits from BaseCaching and implements a LIFO (Last In, First Out) caching system.

put(self, key, item): Adds the item to the cache dictionary. If key or item is None, does nothing. If the cache exceeds MAX_ITEMS, the last item added is discarded.
get(self, key): Returns the value associated with key in the cache dictionary. If key is None or does not exist, returns None.
3. LRU Caching
Create a class LRUCache that inherits from BaseCaching and implements an LRU (Least Recently Used) caching system.

put(self, key, item): Adds the item to the cache dictionary. If key or item is None, does nothing. If the cache exceeds MAX_ITEMS, the least recently used item is discarded.
get(self, key): Returns the value associated with key in the cache dictionary. If key is None or does not exist, returns None.
4. MRU Caching
Create a class MRUCache that inherits from BaseCaching and implements an MRU (Most Recently Used) caching system.

put(self, key, item): Adds the item to the cache dictionary. If key or item is None, does nothing. If the cache exceeds MAX_ITEMS, the most recently used item is discarded.
get(self, key): Returns the value associated with key in the cache dictionary. If key is None or does not exist, returns None.
5. LFU Caching (Advanced)
Create a class LFUCache that inherits from BaseCaching and implements an LFU (Least Frequently Used) caching system.

put(self, key, item): Adds the item to the cache dictionary. If key or item is None, does nothing. If the cache exceeds MAX_ITEMS, the least frequently used item is discarded. If there are ties, the least recently used item among them is discarded.
get(self, key): Returns the value associated with key in the cache dictionary. If key is None or does not exist, returns None.
Repository
GitHub repository: alx-backend
Directory: 0x01-caching
Each caching system implementation should be in its respective Python file within the directory. The implementations must adhere to the specified requirements and constraints.