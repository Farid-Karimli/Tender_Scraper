import requests
from bs4 import BeautifulSoup
import googlesearch
import time
from urllib3.exceptions import InsecureRequestWarning

import func
from urllib.parse import urlparse
import warnings
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

# func.get_links()
tender_data = {}
total_tenders = 0

# links = func.get_links()
links = open("tender_links.txt", 'r')

"""for link in links:
    print(link)
    link = link.replace("\n",'')
    t = urlparse(link).netloc
    if 'www' not in t:
        domain =  '.'.join(t.split('.')[0:])
    else:
        domain = '.'.join(t.split('.')[1:])
    print(domain)

    if ".pdf" in link:
        print('Error: Requested file is a PDF file. ')
        print()
        tender_data[domain] = 'Does not have tender announcements'
        continue
    else:
        print('connecting to', domain)

    page = requests.get(link, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = str(soup.title)

    if title == '' or title is None:
        print('Title does not exist or is empty.')
        tender_data[domain] = 'Does not have tender announcements'
        continue
    else:
        title = title.replace("<title>", "").replace('</title>', '')
        print("Title: ", title.strip())
        print()

    many_tenders = func.many_tenders(soup)
    organization = func.check_organization(soup, domain)

    if many_tenders:
        print('Many tenders')
        tenders = func.parse_page(soup)
        print('tenders =', tenders)
        total_tenders += tenders
    else:
        tenders = 1
        total_tenders += 1

    tender_data[domain] = [organization, tenders, link]"""

    # page.close()













page = requests.get("https://fed.az/az/tenderler", verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
# title = str(soup.title)
print(func.many_tenders((soup)))
many_tenders = func.many_tenders(soup)
if many_tenders:
    print('Many tenders')
    tenders = func.parse_page(soup)
    print('tenders =', tenders)
    total_tenders += tenders
else:
    tenders = 1
    total_tenders += 1
print('total_tenders =', total_tenders)