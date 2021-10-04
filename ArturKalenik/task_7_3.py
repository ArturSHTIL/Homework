import time
import requests


def benchmark_time(func):
    """
    Implement decorator with context manager support for writing execution time to log-file.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        with open('example3.txt', 'a') as data:
            data.write('[*] Execution time: {} seconds.'.format(end - start) + '\n')

        return return_value

    return wrapper


@benchmark_time
def fetch_webpage(url):
    web_page = requests.get(url)
    return web_page


if __name__ == '__main__':
    webpage = fetch_webpage('https://google.com')
