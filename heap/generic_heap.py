class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        return_value = self.storage.pop()
        self._sift_down(0)
        return return_value

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2

        if index == 0:
            return
        else:
            if self.comparator(self.storage[index], self.storage[parent_index]):
                self.storage[index], self.storage[parent_index] \
                    = self.storage[parent_index], self.storage[index]
                self._bubble_up(parent_index)

    def _sift_down(self, index):
        index_left_child = index * 2 + 1
        index_right_child = index * 2 + 2

        if index_left_child >= self.get_size():
            return

        elif self.comparator(self.storage[index], self.storage[index_left_child]) \
                and self.comparator(self.storage[index], self.storage[index_right_child]):
            return

        else:
            if index_right_child >= self.get_size():
                switch_index = index_left_child
            else:
                switch_index = index_left_child \
                    if self.comparator(
                        self.storage[index_left_child], self.storage[index_right_child]) \
                    else index_right_child

            self.storage[index], self.storage[switch_index] \
                = self.storage[switch_index], self.storage[index]
            self._sift_down(switch_index)
