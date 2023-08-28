# webScraper

## Goal
I want to make a web scraper in Python and figure out how such an application:
- is best built (which libraries, what architecture, etc.)
- is able to extract data from websites (only pure HTML or also cookies or other cached data?)
- is configurable to be able to extract data from various websites


## General Development Path:
1. Read 1-2 articles on web scraping in Python and make notes related to points above
2. Look at opensanctions to see how they implement web scraping
3. Build a proof-of-concept with a chosen, basic website (e.g., a wikipedia page)
4. Extend PoC to be able to handle a more complex website (e.g., zalando.de)
5. Write and test foundational application that is:
   1. easily extensible to more websites
   2. fast
   3. able to store data in a consistent and convenient format

## Learning Notes

### realpython.com article
[Practical intro to Python web scraping](https://realpython.com/python-web-scraping-practical-introduction/)



---

### recommended modules

**Conclusions:**
1. Start with BeautifulSoup - it's the simplest library to learn and can help me learn the basics
2. Upgrade to Scrapy and investigate what other features I can incorporate
3. Consider using LXML library for parsing (if it's faster)
4. See how to use Selenium (particularly for Javascript)


#### Beautiful soup
Beautiful soup creates a tree of the HTML (or XML) structure from an HTML string object

**Notes:** it's 'HTMLparser' can be slow apparently

---

#### LXML
XML and HTML parser. Can be fast, but apparently can have issues with broken HTML and is apparently not documented very well and can have some 'manual memory management' issues.

---

#### Scrapy
Open-source tool; provides some additional built-in tools for monitoring crawlers + dealing with cookies + user-agent spoofing, etc.

**Note:** Prefer this since it's open-source?

---

#### Selenium
A library to support 'web browser automation'. Includes an IDE and allows running tests

**Note:**  I still don't really understand this library yet.

---

#### Mechanical Soup
As opposed to BeautifulSoup, MechanicalSoup provides ways to interact with web pages via its 'headless browser'.

---

**Sources:**
- [aimultiple.com article](https://research.aimultiple.com/python-web-scraping-libraries/)
- [projectpro.io article](https://www.projectpro.io/article/python-libraries-for-web-scraping/625)


---

