from utils import sorting_test


class RadixSort:
    @staticmethod
    def sort(arr: list):
        rad = 10

        while True:
            rad_list = [[] for _ in range(10)]
            for num in arr:
                r = num % rad // (rad // 10)
                rad_list[r].append(num)

            if not any(rad_list[1:]):
                return rad_list[0]

            arr.clear()
            for r_list in rad_list:
                if r_list:
                    arr += r_list

            rad *= 10


if __name__ == '__main__':
    rs = RadixSort()
    sorting_test(rs.sort)
