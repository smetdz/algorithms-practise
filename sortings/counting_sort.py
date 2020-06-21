from utils import sorting_test


class CountingSort:
    @staticmethod
    def sort(arr: list) -> list:
        counting_arr = [0 for _ in range(0, max(arr) + 1)]

        for num in arr:
            counting_arr[num] += 1

        offset = 0
        for i, num in enumerate(counting_arr):
            arr[offset: offset + num] = [i for _ in range(num)]
            offset += num

        return arr


if __name__ == '__main__':
    cs = CountingSort()
    sorting_test(cs.sort)
