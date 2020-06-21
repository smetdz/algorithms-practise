from utils import sorting_test


class MergeSort:
    def sort(self, arr: list) -> list:
        if len(arr) <= 1:
            return arr

        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        left = self.sort(left)
        right = self.sort(right)

        result = self.merge(left, right)

        return result

    @staticmethod
    def merge(left: list, right: list) -> list:
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result += left
        elif right:
            result += right

        return result


if __name__ == '__main__':
    ms = MergeSort()
    sorting_test(ms.sort)
