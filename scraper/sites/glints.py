from bs4 import BeautifulSoup
from rich import print


def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def browser_controller(driver, link):
    driver.get(link)
    # find_element, click
    print('Glints driver success opening page')
    return driver.page_source

def get_page(driver, link):
    html = browser_controller(driver, link)
    soup = BeautifulSoup(html, 'html.parser')
    job_list = soup.find_all('div', class_='JobCardsc__JobcardContainer-sc-hmqj50-0 iirqVR CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-5 hRilQl')
    print(job_list)
    
    list = []
    for job in job_list:

        #parsing desk
        desk = job.find('a')
        desk = desk.text.strip()

        #parsing company
        company = job.find('div', class_='Box__StyledBox-sc-pr7b7l-0 kgsHid Flex__StyledFlex-sc-11ryoct-0 evNJxH CompactOpportunityCardsc__CompanyInformation-sc-dkg8my-15 GCUkw')
        company = company.find('a').text.strip()
        
        #parsing location
        location = job.find('div', class_='CompactOpportunityCardsc__OpportunityInfo-sc-dkg8my-20 ipFwqI')
        location = location.text.strip()

        #parsing link
        link = job.find('a')
        link = 'https://www.glints.com' + link.get('href')

        #parsing salary
        salary = job.find('div', class_='CompactOpportunityCardsc__JobTitleSalaryWrapper-sc-dkg8my-10 iZSAsS')
        salary = salary.find('span').text.strip()
        
        dict = {
            'desk' : desk,
            'company' : company,
            'location' : location,
            'link' : link,
            'salary' : salary.replace('\xa0', '')
        }
        list.append(dict)
    print(f'Glints got {len(job_list)} data')
    return list

if __name__=='__main__':
    get_page()
