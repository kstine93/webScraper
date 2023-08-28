'''
Basic_scraper

The purpose of this page is to just demonstrate various ways
to implement web scraping in python using various modules.

This follows, in part, the tutorial on realpython.com:
https://realpython.com/python-web-scraping-practical-introduction/
'''

#--------------
import requests
from bs4 import BeautifulSoup
import mechanicalsoup

#--------------
site_1 = "http://olympus.realpython.org/profiles/dionysus"
site_2 = "http://olympus.realpython.org/login"

#--------------
def scraper_1():
    """Uses BeautifulSoup and Requests to parse basic HTML"""
    res = requests.get(site_1)
    res = res.content #Need to use .decode('utf-8')?

    soup = BeautifulSoup(res,"html.parser")

    print(soup.get_text()) #removes tags - only produces text.

    images = soup.find_all('img')
    print(images[0])
    print(type(images[0]))
    print(images[0]['src']) #You can use indexing to get values - beautiful soup does this.

    #You can help bs4 filter down what you need by providing extra information:
    target = soup.find_all('img',src='/static/dionysus.jpg')
    print(target)

#--------------
def scraper_2():
    """use mechanical soup to get pages and interact with them"""
    browser = mechanicalsoup.Browser()
    page = browser.get(site_2)
    html = page.soup

    un = 'zeus'
    pw = 'ThunderDude'


    form = html.form
    form.find("input",attrs={"name":"user"})['value'] = un
    form.find("input",{"name":"pwd"})['value'] = pw

    res = browser.submit(form,site_2)
    print(res.url)


#==============
if __name__ == "__main__":
    func = scraper_2
    print(f"Running scraper: {func.__name__}\n-------")
    func()