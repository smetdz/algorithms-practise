from utils import sorting_test


class InsertionSort:
    @staticmethod
    def sort(arr: list) -> list:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key

        return arr


if __name__ == '__main__':
    i_s = InsertionSort()
    sorting_test(i_s.sort)
