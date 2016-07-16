
from collections import defaultdict
from pprint import pprint
import json
import re
import xml.etree.cElementTree as ET

import scrape
scrape_table = scrape.ScrapeTable()

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit_street_type(street_types, file):
    osm_file = open(file, "r")
    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    m = street_type_re.search(tag.attrib["v"])
                    if m:
                        street = m.group()
                        if not scrape_table.has_suffix(street):
                            street_types[street].add(tag.attrib["v"])



def clean_street(street_name):

    street_split = street_name.split(" ")

    for i in range(len(street_split)):

        if scrape_table.has_suffix(street_split[i]):
            street_split[i] = scrape_table.convert_suffix(street_split[i])

    return ' '.join(street_split)


def main():

    street_types = defaultdict(set)
    audit_street_type(street_types,'data/sample.osm')
    street_types = dict(street_types)

    for key in street_types:
        street_types[key] = list(street_types[key])

    json.dump(street_types,open('data/streetTypes.json','w'),sort_keys=True, indent=2)

if __name__=='__main__':
    main()

