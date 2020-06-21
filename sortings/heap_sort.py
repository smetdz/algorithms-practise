from utils import sorting_test


class HeapSort:
    def sort(self, arr: list) -> list:
        arr = self.build_heap(arr)
        heap_size = len(arr)

        for i in range(len(arr) - 1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heap_size -= 1
            arr = self.heapify(arr, 0, heap_size)

        return arr

    @staticmethod
    def largest_check(arr: list, largest: int, other: int, heap_size: int) -> int:
        if other < heap_size and arr[other] > arr[largest]:
            largest = other

        return largest

    def heapify(self, arr: list, ind: int, heap_size: int) -> list:
        left = 2 * ind + 1
        right = 2 * ind + 2
        largest = ind

        largest = self.largest_check(arr, largest, left, heap_size)
        largest = self.largest_check(arr, largest, right, heap_size)

        if largest != ind:
            arr[largest], arr[ind] = arr[ind], arr[largest]
            arr = self.heapify(arr, largest, heap_size)

        return arr

    def build_heap(self, arr: list) -> list:
        for i in range(int(len(arr)), -1, -1):
            self.heapify(arr, i, len(arr))

        return arr


if __name__ == '__main__':
    hs = HeapSort()
    sorting_test(hs.sort)
