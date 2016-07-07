#!/Users/ashir/Downloads/env/bin/python
from bs4 import BeautifulSoup
import urllib2
from collections import  defaultdict
import unicodedata

class ScrapeTable():

    def __init__(self):
        self.data = defaultdict(set)

        content = urllib2.urlopen("http://www.expertmarket.com/USPS-street-suffix").read()
        soup = BeautifulSoup(content,"html.parser")
        rows = soup.find('table').contents
        #print rows
        total = 0
        word = ""
        for row in rows:
            total+=1
            if (total ==1):
                continue

            abc = str.strip(unicodedata.normalize('NFKD', row.contents[0].get_text()).encode('ascii','ignore'))

            if abc != '':
                word = abc
                self.data[word].add(str(row.contents[1].get_text()).lower())
            else:
                self.data[word].add(str(row.contents[1].get_text()).lower())

        self.data = dict(self.data)

    def has_suffix(self,value):
        for key, val in self.data.iteritems():
            if value.lower() in val:
                print str(key).capitalize()


    def prints(self):

        print(self.data)

    def __str__(self):
         return dict(self.data)


def main():
    url = 'http://www.expertmarket.com/USPS-street-suffix'
    abcd = ScrapeTable()

    abcd.has_suffix("BLVD")

if __name__=='__main__':
    main()