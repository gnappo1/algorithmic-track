from time import time


def test_python():
    x = list(range(100_000_000))
    t0 = time()
    y = [i * 2 for i in x]
    print("Python:", time() - t0)


def test_numpy():
    import numpy as np

    x = np.arange(100_000_000)
    t0 = time()
    y = x * 2
    print("Numpy:", time() - t0)


test_python()
test_numpy()
