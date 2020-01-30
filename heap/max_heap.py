import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        pass

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
        pass


# test = Heap()

# print(test._bubble_up(1))
# print(test._bubble_up(2))
# print(test._bubble_up(3))
# print(test._bubble_up(4))
# print(test._bubble_up(5))
# print(test._bubble_up(6))
# print(round(0.5))
# print(round(1.5))
# print(round(2.7))
# print(round(3.5))
