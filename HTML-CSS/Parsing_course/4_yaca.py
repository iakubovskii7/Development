import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    r = requests.get(url)
    if r.ok: # 200  ## 403 404
        return r.text
    print(r.status_code)


def refine_cy(s):
    # ТИЦ: 500000 -> ['ТИЦ:', '500000']
    return s.split(' ')[-1]


def write_csv(data):
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['snippet'],
                         data['cy']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    lis = soup.find_all('li', class_='yaca-snippet')

    for li in lis:
        try:
            name = li.find('h2').text
        except:
            name = ''

        try:
            url = li.find('h2').find('a').get('href')
        except:
            url = ''

        try:
            snippet = li.find('div', class_='yaca-snippet__text').text.strip()
        except:
            snippet = ''

        try:
            c = li.find('div', class_='yaca-snippet__cy').text.strip()
            cy = refine_cy(c)
        except:
            cy = ''

        data = {'name': name,
                'url': url,
                'snippet': snippet,
                'cy': cy}

        write_csv(data)



def main():
    pattern = 'https://yandex.ru/yaca/cat/Entertainment/{}.html'

    for i in range(0, 5):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()
