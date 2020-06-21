from random import randint


def sorting_test(sort_method: staticmethod) -> None:
    test_arr = [randint(0, 100) for _ in range(100)]
    print(test_arr)
    sorted_arr = test_arr

    try:
        sorted_arr = sort_method(test_arr.copy())
        assert sorted_arr == sorted(test_arr)
        print(sorted_arr)
        print('Nice')
    except AssertionError:
        print(sorted_arr)
        print('Sorting does not work')