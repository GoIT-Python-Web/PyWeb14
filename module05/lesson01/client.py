import requests

from time import perf_counter
from concurrent.futures import ThreadPoolExecutor

URLS = ['http://127.0.0.1:5000'  for _ in range(100)]

def call(url):
    print('calling url')
    return requests.get(url)



start = perf_counter()
resultes = ThreadPoolExecutor().map(call, URLS)

for _ in resultes:
    print(_)
print(f"TAKE {perf_counter() -start}")
