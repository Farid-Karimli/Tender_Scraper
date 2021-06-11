import requests
from bs4 import BeautifulSoup
import googlesearch
import time
import func
from urllib.parse import urlparse

# scraper.get_links()
tender_data = {}

links_10 = ['http://sdf.gov.az/az/generic/event/Detail/285/28',  # random 10 links from the get_links() function
            # 'https://www.azadliq.org/a/qarabagi-tiken-shirketler/31235984.html',
            'https://www.oilfund.az/index.php/fund/press-room/advertisements/101',
            'http://www.azerbaijan-news.az/view-116581/baki-seher-icra-hakimiyyeti-menzil-kommunal-teserrufati-departamentinin-aciq-tender-elani',
            'http://www.respublica-news.az/index.php/dig-r-x-b-rl-r/reklam-v-elanlar/item/31467-tender-elanlari',
            'https://bsc.az/news/korporativ-m%C9%99hsullar%C4%B1n-istehsal%C4%B1-%C3%BCzr%C9%99-tender-elan%C4%B1',  #
            'https://www.adb.org/sites/default/files/institutional-document/32150/procurement-guidelines-az.pdf',
            # PROBLEM: pdf file
            'https://genprosecutor.gov.az/az/post/2222',
            'https://www.facebook.com/tender.satinalma.techizat/posts/daha-bir-maraql%C4%B1-tender-elan%C4%B1n%C9%99qliyyat-rabit%C9%99-v%C9%99-y%C3%BCks%C9%99k-texnologiyalar-nazirliyi/2885955568085994/',
            'https://tourism.gov.az/page/tenders?page=2',
            ]

url = links_10[4]

for link in links_10:
    t = urlparse(link).netloc
    domain = '.'.join(t.split('.')[1:])

    if ".pdf" in link:
        print('Requested file is a PDF file.')
    else:
        print('connecting to', domain)

    page = requests.get(link, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = str(soup.title)
    if title == '' or title is None:
        print('Title does not exist or is empty.')
    else:
        title = title.replace("<title>", "").replace('</title>', '')
        print(title)
        print()

    title_valid = func.check_title(title)

    if title_valid:

        tender_data[domain] = 'Has tender announcements'

    page.close()

print(tender_data)