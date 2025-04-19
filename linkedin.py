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

        #parsing desk
        desk = job.find('h3', class_='base-search-card__title').text.strip()
        desk = desk.replace('\n', '')

        #parsing company
        company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        company = company.replace('\n', '')

        #parsing location
        location = job.find('span', class_='job-search-card__location').text.strip()
        location = location.replace('\n', '')

        #parsing link
        link = job.find('a', class_='base-card__full-link').get('href')
        link = 'https://www.linkedin.com' + link

        #parsing salary
        fee = "-"

        dict = {
            'desk' : desk,
            'company' : company,
            'location' : location,
            'link' : link,
            'salary' : fee
        }
        job_list.append(dict)
        
    print(f'linkedin success')
    return job_list
     
if __name__=='__main__':
   html = open_file('linkedin.html')
   get_page(html)