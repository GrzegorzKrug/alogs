import time


def timeit(ammount=10):
    def _timeit(function):
        def wrapper(*args, **kwargs):
            time0 = time.time()
            results = []
            for n in range(ammount):
                result = function(*args, **kwargs)
                results.append(result)

            timeend = time.time()
            duration = timeend - time0

            print(f"Whole run took:  {duration:>3.04f}s")
            print(f"Single run took: {duration / ammount:>3.05f}s")
            return results

        return wrapper

    return _timeit
