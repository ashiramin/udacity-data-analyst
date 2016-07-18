
from pymongo import MongoClient
from pprint import pprint
import operator
import xml.etree.cElementTree as ET
import json
def count_tags(file_name):
    tags = {}
    tag_elements = {}
    for ev,elem in ET.iterparse(file_name):
        tag = elem.tag
        if tag not in tags.keys():
            tags[tag] =1
        else:
            tags[tag] +=1

        if tag == 'tag' and 'k' in elem.attrib:
            if elem.get('k') not in tag_elements.keys():
                tag_elements[elem.get('k')] = 1
            else:
                tag_elements[elem.get('k')] += 1

    kist = list(tag_elements.keys())
    tag_elements = sorted(tag_elements.items(), key=operator.itemgetter(1))


    return tags,tag_elements,kist




def main():

    tags,tagss,tags_list = count_tags('data/sample.osm')

    file = open('data/tagsList.txt','w')
    file.write(','.join(tags_list))

    pprint(tags_list)
    json.dump(dict(tagss),open('data/count_tags.json','w'),indent= 2, sort_keys= True)



if __name__ == '__main__':
    main()