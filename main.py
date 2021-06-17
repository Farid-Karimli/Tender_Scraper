import requests
from bs4 import BeautifulSoup
import googlesearch
from urllib3.exceptions import InsecureRequestWarning
import func
from urllib.parse import urlparse
import warnings

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

# func.get_links()
tender_data = {}


# links = func.get_links()
links = open("tender_links.txt", 'r')


def find_tenders():

    total_tenders = 0
    for link in links:

        print(link)
        link = link.replace("\n", '')
        t = urlparse(link).netloc

        if 'www' not in t:
            domain = '.'.join(t.split('.')[0:])
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
        try:
            page = requests.get(link, verify=False)
        except ConnectionResetError:
            print('Couldn\'t connect, retrying...')
            page = requests.get(link, verify=False)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = str(soup.title)

        soup = BeautifulSoup(page.content, 'html.parser')
        title = str(soup.title)
        if title is None or title == '':
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
            print('Many tenders', many_tenders)
            tenders = func.parse_page(soup)
            print('tenders =', tenders)
            total_tenders += tenders
        else:
            tenders = 1
            print('tenders =', tenders)
            total_tenders += tenders

        tender_data[domain] = [organization, tenders, link]




        page.close()
    print(total_tenders)
    return total_tenders, tender_data


def test_page(link):
    page = requests.get(link, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = str(soup.title)

    many_tenders = func.many_tenders(soup)
    print('Many tenders?', many_tenders)

    print()

    if many_tenders:
        total_tenders = func.parse_page(soup)
    else:
        total_tenders = 1

    print('total_tenders =', total_tenders)
        
        
#test_page('http://finsaz.ru/tender/233943/socar-tender-elan-edib-siyahi/')
tenders = find_tenders()