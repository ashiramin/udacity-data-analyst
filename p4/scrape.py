#!/Users/ashir/Downloads/env/bin/python
from bs4 import BeautifulSoup
import urllib2
from collections import  defaultdict
import unicodedata

custom_addons = {
    "North" : ["N","North"],
    "South" : ["S","South"],
    "West" : ["W","West"],
    "East" : ["E","East"],
    "Highway" : list("Hwy"),
    "Interstate": ["I35","IH","IH35"],
    "Drive" : ["Dr."],
    "Street": ["St."]
}



class ScrapeTable():

    def __init__(self):
        self.data = defaultdict(set)

        content = urllib2.urlopen("http://www.expertmarket.com/USPS-street-suffix").read()
        soup = BeautifulSoup(content,"html.parser")
        rows = soup.find('table').contents
        total = 0
        word = ""
        for row in rows:
            total+=1
            if (total ==1):
                continue

            full_name = str.strip(unicodedata.normalize('NFKD', row.contents[0].get_text()).encode('ascii','ignore'))

            if full_name != '':
                word = full_name
                self.data[word].add(str(row.contents[1].get_text()).lower())
            else:
                self.data[word].add(str(row.contents[1].get_text()).lower())

        self.data = dict(self.data)
        self.data.update(custom_addons)

    def has_suffix(self,value):
        for key, val in self.data.iteritems():
            if value.lower() in str(val).lower():
                return True

        return False

    def convert_suffix(self,value):
        for key, val in self.data.iteritems():
            if value.lower() in str(val).lower():
                return key

    def prints(self):

        print(self.data)

    def __str__(self):
         return dict(self.data)


def main():
    scrape = ScrapeTable()


    assert scrape.has_suffix("North") == True

if __name__=='__main__':
    main()