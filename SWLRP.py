import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("--url", dest="URL", metavar="url", help="URL for the requested page. Only http is stable supported.", required=True)

def uniquelistitems(listurl1):
    unique_list1 = []
    for item in listurl1:
        if item not in unique_list1:
            unique_list1.append(item)
    return unique_list1

def URLParseLinks():
    reqs = requests.get(args.URL)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    unique_list = uniquelistitems(urls)
    for linkurl in unique_list:
        print(linkurl)
    print("\nThe amount of urls on this page: %s" %(len(urls)))
    print("The amount of unique urls on this page: %s" %(len(unique_list)))

if __name__ == "__main__":
    args = parser.parse_args()
    print("Simple Webpage Link Reference Parser v1.0.2\n")
    URLParseLinks()