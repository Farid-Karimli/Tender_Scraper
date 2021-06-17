
import googlesearch
import requests
import multiprocessing
# Initiating the search
from bs4 import BeautifulSoup


def get_links():
    tender_links = []
    f = open('tender_links.txt', 'w')
    query = "tender elanı elan 2020 \"tender \""
    count = 0
    for j in googlesearch.search(query, tld="com", num=1000,stop=500, pause=7, country='AZ'):
        count += 1
        print(j)
        tender_links += [j]
        if count % 10 == 0:
            print('------------------------------------------------')
        f.write(j+"\n")
    f.close()
    print(count,'websites found.')
    return tender_links

def connect_to_link(link):
    page = requests.get(link, verify=False)
    return page

def connect_to_page(link):
    return

def parse_page(soup): #this function should parse any page that has multiple tender announcements in it, returns number of announcements in the page

    tags = soup.find_all("a")
    count = 0

    for tag in tags:
        #print(tag.attrs)
        has_href = 'href' in tag.attrs

        if has_href:
           has_href = len(tag['href']) > 5

        if has_href:
            tag_href = tag['href']

        #print('tag attrs', tag.attrs)
        #print(tag.string)

        # print(has_href)
        #print('----')

        #print(tag.text)
        link_text = tag.text
        text = soup.text

        if has_href and (("elan" in tag_href) or ("elani" in tag_href)):
            #print('a')
            # print('found =', (("elan" in tag_href) or ("elani" in tag_href)))
            count += 1
        elif link_text and ' elan edir ' in link_text or ' elani ' in link_text or ' elan ' in link_text:
            #print('b')
            count += 1

    count_tenders = text.lower().count('elan edir')
    count += count_tenders
    return count



def check_title(title): #this function will check if the given title of a webpage is valid (something we need)
    return ('elan' in title.lower() or 'elanı' in title.lower()) and ('tender' in title.lower() or 'tenderlər' in title.lower())



def many_tenders(soup): # this function will check the contents of the page for keywords that indicates that the page contains a tender announcement
    multiple_tenders = False
    # check the title first
    title = str(soup.title)
    title_is_valid = check_title(title)
    text = str(soup.text)
    print(text)
    if title_is_valid:

        if 'elan' in title.lower() or 'tender' in title.lower():
            print(3)
            multiple_tenders = False
            if text.lower().count('elan edir') > 1:
                print(5)
                multiple_tenders = True
        elif 'elanlar' in title.lower() or 'tenderlər' in title.lower() or  'elanları' in title.lower():
            print(4)
            multiple_tenders = True

    else: #now check the contents of the

        if 'tenderlər' in text.lower() or ' elanlar ' in text.lower() or (text.lower().count('elan edir') > 1) or (text.lower().count('tender elanı') > 1) or (text.lower().count('tender elanları') > 1):
            print(1)
            multiple_tenders = True
        elif text.lower().count(' elan edir ') == 1:
            print(2)
            multiple_tenders  = False

    #print(text)
    print('count of tenders', (text.lower().count('elan edir')))
    return multiple_tenders

def check_organization(soup,domain): # this function will check if the page is from a government organization, or a private company/corporation; returns either 'private' or 'government'
    # check the title first
    organization = ''
    title = str(soup.title).lower()

    if 'dövlət' in title:
        organization = "government"
    else:  # now check the contents of the page
        text = str(soup.text).lower()
        if ("gov.az" in domain or "gov" in domain) or ("Azərbaycan Respublikası Dövlət".lower() in text):
            organization = "government"
        else:
            organization = "private"
    return organization

