from random import randint


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


if __name__ == '__main__':
    test_arr = [randint(0, 100) for _ in range(100)]
    print(test_arr)

    b = BubbleSort()
    try:
        sorted_arr = b.modified_sort(test_arr)
        assert sorted_arr == sorted(test_arr)
        print(sorted_arr)
        print('Nice')
    except AssertionError:
        print('Sorting does not work')
