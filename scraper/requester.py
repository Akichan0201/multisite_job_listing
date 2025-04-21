"""
This module create a requester object that:
- return a headless driver
"""
import requests

from selenium import webdriver

def get_req(link=str):
    r = requests.get(link)
    
    if r.status_code == 200:
        return r.text
    else:
        print(f'error: status code {r.status_code}')
        
def get_sele():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('detach', True)
    agent="Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36"
    options.add_argument(f'user-agent={agent}')
    options.add_argument('--start-maximized')
    options.add_argument('--headless')

    driver = webdriver.Chrome(options)
    # driver.get(link)

    print('Driver has opened')
    return driver
    