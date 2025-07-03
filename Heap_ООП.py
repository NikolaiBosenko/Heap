from abc import ABC, abstractmethod

class Heap_helping_methods(ABC):

    @abstractmethod
    def _one_child(self, index, heap):
        self._index = index
        self._heap = heap
        return self._index*2+1 == len(self._heap)-1

    @abstractmethod
    def _two_children(self, index, heap):
        self._index = index
        self._heap = heap
        return self._index*2+2 <= len(self._heap)-1

    @abstractmethod
    def _is_leaf(self, index, heap):
        self._index = index
        self._heap = heap
        return self._index*2+1 > len(self._heap)-1

    @abstractmethod
    def _is_root(self, index):
        self._index = index
        return self._index == 0

class Heap(Heap_helping_methods):
    def __init__(self, *args):
        self._heap = args

    def get_numbers(self):
        return self._heap

    def _swift_up(self, el, ind):
        self._el = el
        self._index = ind
        if self._index == 0:
            print("Элемент в корне, swift up завршен!")
            return self._heap
        if self._heap[self._index] > self._heap[self._index//2]:
            print("Куча отсортирована!")
            return self._heap
        if self._heap[self._index] < self._heap[self._index//2] and ind//2 >= 0:
            self._heap[self._index], self._heap[self._index // 2] = self._heap[self._index//2], self._heap[self._index]
        return self._swift_up(self, self._el, self._index//2)

    def _swift_down(self, el, ind):
        self._index = ind
        self._el = el

        if self._index*2+1 > len(self._heap) - 1:
            return self._heap

        if self._two_children(self._index, self._heap):
            if self._heap[self._index] > self._heap[self._index*2+1] and self._heap[self._index] > self._heap[self._index*2+2]:

                if self._heap[self._index*2+1] < self._heap[self._index*2+2]:
                    self._heap[self._index], self._heap[self._index*2+1] = self._heap[self._index*2+1], self._heap[self._index]
                    self._index = self._index*2+1

                else:
                    self._heap[self._index], self._heap[self._index*2+2] = self._heap[self._index*2+2], self._heap[self._index]
                    self._index = self._index*2+2

        elif self._one_child(self._index, self._heap):

            if self._heap[self._index*2+1] < self._heap[self._index]:
                self._heap[self._index * 2 + 1], self._heap[self._index] = self._heap[self._index], self._heap[self._index*2+1]
                self._index = self._index*2 + 1



    def add(self, x):
        self._x = x
        self._heap.append(self._x)
        self._index = len(self._heap)
        return self._swift_up(self, self._x, len(self._heap))

    def get_min(self):
        return self._heap[0]

