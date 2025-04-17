'''
- minimal 5000 data(dari mana saja)
- lokasi indonesia
- perusahaan, job desk, gaji, alamat, link
'''

from inisiation import get_req, get_sele
from linkedin import get_page
from exportex import export_data

def test_scrape(link):
    html = get_req(link)
    page = get_page(html)
    export_data(page, 'linkedin.csv')

    print(page)

if __name__=="__main__":
    test_scrape('https://www.linkedin.com/jobs/search/?keywords=python&location=Indonesia')
