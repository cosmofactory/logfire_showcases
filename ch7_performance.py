from time import sleep, time
from typing import Callable

import logfire


@logfire.instrument()
def decorated_func(sleep_time: float) -> None:
    sleep(sleep_time)
    logfire.info("Sleeping for {sleep_time} seconds", sleep_time=sleep_time)


def clean_func(sleep_time: float) -> None:
    sleep(sleep_time)


def main(func: Callable, sleep_time: float) -> None:
    start = time()
    for _ in range(20):
        func(sleep_time)
    end = time()
    print(f"Execution time: {end - start:.2f} seconds")


if __name__ == "__main__":
    logfire.configure()
    sleep_time = 0.5
    main(decorated_func, sleep_time)
    main(clean_func, sleep_time)
