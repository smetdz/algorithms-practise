from utils import sorting_test


class BubbleSort:
    @staticmethod
    def sort(array: list) -> list:
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array

    @staticmethod
    def modified_sort(array: list) -> list:
        ext_ind = len(array) - 1
        while ext_ind > 0:
            last_swap_place = 0
            for i in range(ext_ind):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    last_swap_place = i
            ext_ind = last_swap_place

        return array

    @staticmethod
    def shaker_sort(array: list) -> list:
        left = 0
        right = len(array) - 1
        while left <= right:
            for i in range(left, right):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            right -= 1

            for i in range(right, left, -1):
                if array[i] < array[i - 1]:
                    array[i], array[i - 1] = array[i - 1], array[i]
            left += 1

        return array


if __name__ == '__main__':
    b = BubbleSort()

    print('Simple bubble sort test:')
    sorting_test(b.sort)

    print('Modified bubble sort test:')
    sorting_test(b.modified_sort)

    print('Shaker sort test:')
    sorting_test(b.shaker_sort)
