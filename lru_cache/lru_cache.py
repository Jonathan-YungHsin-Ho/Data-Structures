from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.node_count = 0
        self.list = DoublyLinkedList()
        self.table = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.table.keys():
            return None
        else:
            self.list.move_to_front(self.table[key])
            return self.list.head.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.table.keys():
            self.list.move_to_front(self.table[key])
            self.table[key] = self.list.head
            self.list.head.value = value
        else:
            self.node_count += 1
            self.list.add_to_head(value)
            self.table[key] = self.list.head
        if self.node_count > self.limit:
            self.table = {key: val for key,
                          val in self.table.items() if val != self.list.tail}
            self.list.remove_from_tail()
            self.node_count -= 1
