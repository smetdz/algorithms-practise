from random import randint


class BubbleSort:
    @staticmethod
    def sort(array: list) -> list:
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array


if __name__ == '__main__':
    test_arr = [randint(0, 100) for _ in range(100)]
    print(test_arr)

    b = BubbleSort()
    try:
        sorted_arr = b.sort(test_arr)
        assert sorted_arr == sorted(test_arr)
        print(sorted_arr)
        print('Nice')
    except AssertionError:
        print('Sorting does not work')
