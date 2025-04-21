'''
- minimal 5000 data(dari mana saja)
- lokasi indonesia
- perusahaan, job desk, gaji, alamat, link
'''

"""
This main file will run as CLI:
- accept parameters for sites to scrape [all, linkedin, glints, jobstreet]
- accept parameters for output filename (optional)
"""

from scraper.requester import get_sele
from scraper.sites.linkedin import get_page as linkedin
from scraper.sites.jobstreet import get_page as  jobstreet
from scraper.sites.glints import get_page as glints
from scraper.exporter import export_data


def main():
    glints_link = 'https://glints.com/id/opportunities/jobs/explore?country=ID&locationName=All+Cities%2FProvinces'
    linkedin_link = 'https://www.linkedin.com/jobs/search?keywords=&location=indonesia&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    jobstreet_link = 'https://id.jobstreet.com/id/software-engineer-jobs'

    all_data = []
    driver = get_sele()
    # linkedin_data = linkedin(driver, linkedin_link)
    # jobstreet_data = jobstreet(driver, jobstreet_link)
    glints_data = glints(driver, glints_link)
    print(glints_data)
    driver.quit()
    
    all_data.extend(glints_data)
    # all_data.extend(linkedin_data)
    # all_data.extend(jobstreet_data)

    export_data(all_data, 'output2.xlsx')

if __name__=="__main__":
    main()