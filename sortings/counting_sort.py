from utils import sorting_test


class CountingSort:
    @staticmethod
    def sort(arr: list) -> list:
        counting_arr = [arr.count(i) for i in range(0, max(arr) + 1)]

        offset = 0
        for i, num in enumerate(counting_arr):
            arr[offset: offset + num] = [i for _ in range(num)]
            offset += num

        return arr


if __name__ == '__main__':
    cs = CountingSort()
    sorting_test(cs.sort)
