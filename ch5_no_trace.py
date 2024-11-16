from time import sleep

import logfire


def fast_simple_function():
    sleep(0.2)


def slow_complex_function(number: int) -> int:
    if number % 2 == 0:
        sleep(1)
    return None


def main():
    for i in range(1, 6):
        fast_simple_function()
        slow_complex_function(i)


if __name__ == "__main__":
    main()
