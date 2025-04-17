from bs4 import BeautifulSoup


def open_file(filename):
    with open (filename, 'r', encoding='utf-8') as f:
        return f.read()

def get_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    jobs = soup.find('ul', class_='jobs-search__results-list')
    jobs = jobs.find_all('li')

    job_list = []
    for job in jobs:
        desk = job.find('h3', class_='base-search-card__title').text.strip()
        job_list.append(desk)

    return job_list
     
if __name__=='__main__':
   html = open_file('linkedin.html')
   get_page(html)