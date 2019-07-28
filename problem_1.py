from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache_dict = {}
        self.cache_deque = deque()
        
    def get(self, key):
        if(self.cache_dict.get(key) is None):
            return -1
        else:            
            self.cache_deque.remove(key)
            self.cache_deque.appendleft(key)
            return self.cache_dict.get(key)
        
        
        
        

    def set(self, key, value):
    	if(self.capacity==0):
    		print("Cannot add. Cache has empty capacity")
    		return
    	if(self.cache_dict.get(key) is None):    		
    		if(len(self.cache_deque)==self.capacity):
	    		val= self.cache_deque.pop()
   	 		self.cache_dict.pop(val)
    			self.cache_dict[key]=value
    			self.cache_deque.appendleft(key)
    		else:
    			self.cache_dict[key]=value
    			self.cache_deque.appendleft(key)
    	else:
    		self.cache_dict[key]=value
    		self.cache_deque.remove(key)
    		self.cache_deque.appendleft(key)
            
            
            
our_cache = LRU_Cache()

our_cache.set(1, 1)

our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(1, 1)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print(our_cache.get(2))       # returns 2
our_cache.set(7, 7)
our_cache.set(8, 8)
print(our_cache.get(1))       # returns 1 since it was overwritten
print(our_cache.get(6))       # returns 6
print(our_cache.get(5))       # returns -1 since it was least used
print(our_cache.get(0))       # returns -1 since it is non existent

empty_cache = LRU_Cache(0)
empty_cache.set(1, 1)	#prints Cannot add. Cache has empty capacity since it has 0 capacity
