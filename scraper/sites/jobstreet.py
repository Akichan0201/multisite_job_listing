from bs4 import BeautifulSoup
from rich import print


def open_file(filename):
    with open (filename, 'r', encoding='utf-8') as f:
        return f.read()

def browser_controller(driver, link):
    driver.get(link)
    # find_element, click
    print('Jobstreet driver success opening page')
    return driver.page_source

def get_page(driver, link):
    html = browser_controller(driver, link)
    soup = BeautifulSoup(html, 'html.parser')
    jobs = soup.find('div', id='app')
    jobs = jobs.find_all('article', class_='gg45di0 gg45di1 _1ubeeig8n _1ubeeig8o _1ubeeig7j _1ubeeig7k _1ubeeigav _1ubeeigaw _1ubeeig9r _1ubeeig9s _1ubeeigh _1ubeeig67 _1ubeeig5f efwo40b efwo409 efwo40a _1oxsqkd18 _1oxsqkd1b _1ubeeig33 _1ubeeig36')

    job_list = []
    for job in jobs:

        #parsing desk
        desk = job.find('div', class_='gg45di0 _1ubeeig5h _1ubeeig53')
        desk = desk.text.strip()

        #parsing company
        company = job.find('div', class_='gg45di0 _1ubeeig7v')
        company = company.find('div', class_='gg45di0 _1ubeeig5h _1ubeeig53').text.replace('di ','')

        #parsing location
        location = job.find('div', class_='gg45di0 _1ubeeig5b _1ubeeighf _1ubeeig6n')
        location = location.find('span', class_='gg45di0').text.strip()
        
        #parsing link
        link = job.find('div', class_='gg45di0 _1ubeeig4z _1ubeeig4x')
        link = 'https://www.jobstreet.co.id' + link.find('a').get('href')

        #parsing salary
        salary = '-'

        dict = {
            'desk' : desk,
            'company' : company,
            'location' : location,
            'link' : link,
            'salary' : salary
        }

        job_list.append(dict)

    print(f'Jobstreet got {len(job_list)} data')
    return job_list
