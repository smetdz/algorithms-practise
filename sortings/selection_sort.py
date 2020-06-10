from utils import sorting_test


class SelectionSort:
    @staticmethod
    def sort(arr: list) -> list:
        for i in range(0, len(arr)):
            min_ind = i
            ch_m = False
            for j in range(i + 1, len(arr)):
                if arr[min_ind] > arr[j]:
                    min_ind = j
                    ch_m = True

            if ch_m:
                arr[i], arr[min_ind] = arr[min_ind], arr[i]

        return arr


if __name__ == '__main__':
    ss = SelectionSort()
    sorting_test(ss.sort)
