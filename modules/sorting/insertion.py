import numpy as np
from timeruns import timeit

N = 1000
size = 500


@timeit(N)
def test(size=100):
    array = list(np.random.randint(0, size * 2, size))
    solution = array.copy()

    insertion_in_place(array)
    solution.sort()
    valid = solution == array
    return valid


def insertion_in_place(array):
    for ind in range(1, len(array)):
        elem = array.pop(ind)

        for iner_ind in range(0, ind):
            if elem < array[iner_ind]:
                array.insert(iner_ind, elem)
                break
        else:
            array.insert(ind, elem)


outs = test(size)
valid_amm = len([el for el in outs if el])
print(f"{valid_amm / N * 100:4.2f} % sortings successful")
