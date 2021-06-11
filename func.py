import googlesearch

# Initiating the search

def get_links():
    tender_links = []
    query = "\"tender\" elan OR \"tender\" elanı\""
    count = 0
    for j in googlesearch.search(query, tld="com", num=10,stop=1000, pause=10, country='AZ'):
        count += 1
        print(j)
        tender_links += [j]
        if count % 10 == 0:
            print('------------------------------------------------')

    print(count,'websites found.')


def parse_page(): #this function should parse any page that has multiple tender announcements in it
    return




def check_title(title): #this function will check if the given title of a webpage is valid (something we need)

    is_valid = False
    if ('elan' in title.lower() or 'elanı' in title.lower()) and ('tender' in title.lower() or 'tenderlər' in title.lower()):
        is_valid = True
    return is_valid