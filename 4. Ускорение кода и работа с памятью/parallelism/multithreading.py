import requests
import time
import concurrent.futures
urls = [
  'http://www.python.org',
  'https://docs.python.org/3/',
  'https://docs.python.org/3/whatsnew/3.7.html',
  'https://docs.python.org/3/tutorial/index.html',
  'https://docs.python.org/3/library/index.html',
  'https://docs.python.org/3/reference/index.html',
  'https://docs.python.org/3/using/index.html',
  'https://docs.python.org/3/howto/index.html',
  'https://docs.python.org/3/installing/index.html',
  'https://docs.python.org/3/distributing/index.html',
  'https://docs.python.org/3/extending/index.html',
  'https://docs.python.org/3/c-api/index.html',
  'https://docs.python.org/3/faq/index.html'
  ]


def download_site(url, session):
  with session.get(url) as response:
    print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
  with requests.Session() as session:
    for url in sites:
      download_site(url, session)


def download_all_sites_concur(sites):
  with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(download_site, sites)