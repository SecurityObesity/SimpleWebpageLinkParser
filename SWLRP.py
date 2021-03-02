import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("--url", dest="URL", metavar="url", help="URL for the requested page.", required=True)

def URLParseLinks():
    reqs = requests.get(args.URL)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    uniquelist2 = uniquelistitems(urls)
    printlinks = sortedfullurls(uniquelist2)
    for linkurl in printlinks:
        linkurlitem = linkurl[8:].replace("//","/")
        print(f'{linkurl[:8]}{linkurlitem}')
    print("\nThe amount of urls on this page: %s" %(len(urls)))
    print("The amount of unique urls on this page: %s" %(len(uniquelist2)))

def uniquelistitems(listurl1):
    unique_list1 = []
    for item in listurl1:
        if item not in unique_list1:
            unique_list1.append(item)
    return unique_list1

def sortedfullurls(fullurls):
    fullurlslist = []
    for resitem in fullurls:
        if resitem.startswith("/"):
            fullurlslist.append(f'{args.URL}{resitem}')
        else:
            fullurlslist.append(resitem)
    return fullurlslist

if __name__ == "__main__":
    args = parser.parse_args()
    print("Simple Webpage Link Reference Parser\n")
    URLParseLinks()
