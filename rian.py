from linkedin import open_file

from bs4 import BeautifulSoup as bs


def parse_data(html):
    soup = bs(html, 'html.parser')
    job_list = soup.find('ul', class_='jobs-search__results-list')
    job_list = job_list.find_all('li')

    for job in job_list:
        position = job.find('h3', class_='base-search-card__title').text.strip()
        print(position)


if __name__ == '__main__':
    html = open_file('linkedin.html')
    parse_data(html)