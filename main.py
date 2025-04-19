'''
- minimal 5000 data(dari mana saja)
- lokasi indonesia
- perusahaan, job desk, gaji, alamat, link
'''

from inisiation import get_req, get_sele
from jobstreet import get_page
from export import export_data

def test_scrape(link):
    html = get_req(link)
    page = get_page(html)
    export_data(page, 'jobstreet.csv')

if __name__=="__main__":
    test_scrape('https://id.jobstreet.com/id/jobs?jobId=83416560&type=standard')
