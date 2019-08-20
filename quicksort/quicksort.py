from typing import List


class QuickSort(object):
    """
    Description:
        Quicksort implementation based on the original paper by C. A. R. Hoare (1961).
        All variable names attempts to the naming convention described in his paper.

    Methods:
        partition(lower_pointer: int, upper_pointer: int, bound: int) -> int
        quick_sort(lower_pointer: int, upper_pointer: int) -> None
    """

    def __init__(self, store: List[int]):
        """ Constructor for QuickSort """
        self.store = store
        self.quick_sort(0, len(self.store) - 1)

    def partition(self, lower_pointer: int, upper_pointer: int, bound: int) -> int:
        while lower_pointer < upper_pointer:
            while self.store[lower_pointer] < bound:
                lower_pointer += 1
            while self.store[upper_pointer] > bound:
                upper_pointer -= 1

            self.store[lower_pointer], self.store[upper_pointer] = self.store[upper_pointer], self.store[lower_pointer]
            lower_pointer += 1
            upper_pointer -= 1
        return lower_pointer

    def quick_sort(self, lower_pointer: int, upper_pointer: int) -> None:
        if lower_pointer >= upper_pointer:
            return
        bound = (self.store[round((upper_pointer + lower_pointer) / 2)])
        divider = self.partition(lower_pointer, upper_pointer, bound)
        self.quick_sort(lower_pointer, divider - 1)
        self.quick_sort(divider, upper_pointer)

    def __repr__(self):
        return str(self.store)

    def __getitem__(self, item):
        return self.store[item]


if __name__ == '__main__':
    arr = [1, 5, 7, 2, 3, 8, 4]
    print(QuickSort(arr))
  # print(arr)
