def collatz_conjecture(curr_num):
    if curr_num == 1:
        return 1
    if curr_num % 2 == 0:
        curr_num = curr_num / 2
    else:
        curr_num = 3 * curr_num + 1
    collatz_conjecture(curr_num)



def collatz_conjecture(curr_num):
    if curr_num == 1:
        return 1
    return collatz_conjecture(3 * curr_num + 1 if curr_num % 2 else curr_num / 2) + 1





def memoize(cache=None):
    if cache is None:
        cache = {}
    def wrapper(fn):
        def inner(*args):
            try:
                return cache[args]
            except KeyError:
                r = fn(*args)
                cache[args] = r
                return r
        return inner
    return wrapper


@memoize({(1,): 1})
def collatz_conjecture(n):
    return collatz_conjecture(3 * n + 1 if n % 2 else n / 2) + 1


def main():
    while True:
        user_input = input()
        if not user_input:
            break
        start, end = map(int, user_input.split()[:2])
        print(start, end, max(collatz_conjecture(i) for i in range(start, end + 1)))


if __name__ == '__main__':
    main()
