import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        if self.get_size() == 1:
            return self.storage.pop()
        else:
            last_index = self.get_size() - 1
            self.storage[0], self.storage[last_index] = self.storage[last_index], self.storage[0]
            return_value = self.storage.pop()
            self._sift_down(0)
            return return_value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = math.ceil((index - 2) / 2)
        if index == 0:
            return
        else:
            if self.storage[index] > self.storage[parent_index]:
                self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
                self._bubble_up(parent_index)

    def _sift_down(self, index):
        # print('\n')
        # print('Index', index)
        # print('Value', self.storage[index])
        index_left_child = index * 2 + 1
        index_right_child = index * 2 + 2

        if index_left_child >= self.get_size():
            # print('No children')
            return
        elif self.storage[index] >= self.storage[index_left_child] and self.storage[index] >= self.storage[index_right_child]:
            # print('Larger than children')
            return
        else:
            # print('Needs switch')
            if index_right_child >= self.get_size():
                switch_index = index_left_child
            else:
                switch_index = index_left_child if self.storage[
                    index_left_child] >= self.storage[index_right_child] else index_right_child
            self.storage[index], self.storage[switch_index] = self.storage[switch_index], self.storage[index]
            self._sift_down(switch_index)
