import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

base_url = 'https://chelyabinsk.hh.ru/search/vacancy?L_is_autosearch=false&area=104&clusters=true&enable_snippets=true&search_period=30&text=python&page=0'

def hh_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            jobs = []
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text

            content1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            content2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            content = content1 + ' ' + content2

            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'content': content
            })
            print (jobs)

    else:
        print ('ERROR')

hh_parse(base_url, headers)