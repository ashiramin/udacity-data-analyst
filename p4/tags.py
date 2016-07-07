__author__ = 'ashir'


import ast
import xml.etree.cElementTree as ET
import json
from collections import defaultdict
from pprint import pprint

def audit_tags(tags_list,file_name):

    osm_data = file(file_name,'r')
    results = defaultdict(set)
    for ev,elem in ET.iterparse(osm_data):

        tag = elem.tag

        if tag in ("node","way",):
            for el in elem.iter('tag'):
                if 'k' in el.attrib and 'v' in el.attrib:

                    key = el.get('k')
                    value = el.get('v')

                    if key in tags_list and len(results[key]) < 30:

                        results[key].add(value)

    return results




def main():
    file = open('data/tagsList.txt','r')
    abc = str(file.readlines())
    abc = abc[2:]
    abc = abc[:-2]

    tags_list = abc.split(',')

    result = dict(audit_tags(tags_list,'data/sample.osm'))

    for key in result:
        result[key] = list(result[key])

    json.dump(result,open('data/tags.json','w'),indent= 2, sort_keys= True)
    pprint(result)




if __name__ == '__main__':
    main()