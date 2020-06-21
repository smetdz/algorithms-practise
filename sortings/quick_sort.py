from utils import sorting_test


class QuickSort:
    def __init__(self):
        self.arr = None

    def sort(self, arr: list) -> list:
        self.arr = arr
        self.quick_sort(0, len(self.arr) - 1)

        return self.arr

    def quick_sort(self, low: int, high: int) -> None:
        if low < high:
            part = self.partition(low, high)
            self.quick_sort(low, part - 1)
            self.quick_sort(part + 1, high)

    def partition(self, low: int, high: int) -> int:
        piv = self.arr[high]
        ind = low

        for i in range(low, high):
            if self.arr[i] <= piv:
                self.arr[ind], self.arr[i] = self.arr[i], self.arr[ind]
                ind += 1

        self.arr[ind], self.arr[high] = self.arr[high], self.arr[ind]

        return ind


if __name__ == '__main__':
    qs = QuickSort()
    sorting_test(qs.sort)
