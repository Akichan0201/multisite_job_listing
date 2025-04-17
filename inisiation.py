import requests

from selenium import webdriver

def get_req(link=str):
    r = requests.get(link)
    
    if r.status_code == 200:
        return r.text
    else:
        print(f'error: status code {r.status_code}')
        
def get_sele(link=str):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options)
    driver.get(link)

    return driver
    