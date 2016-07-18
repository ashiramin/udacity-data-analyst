import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
import phonenumbers
import audit

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
address_regex = re.compile(r'^addr\:')
street_regex = re.compile(r'^street')


CREATED = [ "version", "changeset", "timestamp", "user", "uid"]
ALIAS_TAGS = ['name_1', 'old_name', 'alt_name', 'name_2', 'place_name', 'loc_name',
    'official_name', 'name_3', 'short_name']

ZIPCODE_TAGS = [ 'addr:postcode','postal_code' ]
CONTACT_TAGS =  ['contact:phone' , 'phone']

def shape_element(element):
    node = {}
    position_attributes = ['lat', 'lon']
    created_attributes = CREATED
    zipcode_tags = ZIPCODE_TAGS
    contact_tags = CONTACT_TAGS
    alias_tags = ALIAS_TAGS

    if element.tag == "node" or element.tag == "way":
        # populate tag type
        node['type'] = element.tag

        address = {}
        zipcode = set()


        for attribute in element.attrib:
            if attribute in created_attributes:
                if 'created' not in node:
                    node['created'] = {}
                node['created'][attribute] = element.get(attribute)
            elif attribute in position_attributes:
                continue
            else:
                node[attribute] = element.get(attribute)


        if 'lat' in element.attrib and 'lon' in element.attrib:
            node['pos'] = [float(element.get('lat')), float(element.get('lon'))]


        for child in element:

            if child.tag == 'nd':
                if 'node_refs' not in node:
                    node['node_refs'] = []
                if 'ref' in child.attrib:
                    node['node_refs'].append(child.get('ref'))


            if child.tag != 'tag' or 'k' not in child.attrib or 'v' not in child.attrib:
                continue
            key = child.get('k')
            val = child.get('v')

            if problemchars.search(key):
                continue

            # Ignored all tags gnis and  except one
            if key.startswith("gnis") or key.startswith("tiger"):
                if key == 'tiger:county':
                    key = key.replace('tiger','')
                    node[key] = val
                continue

            if key in alias_tags:
                if 'aliases' not in node:
                    node['aliases'] = []

                node['aliases'] = val
                continue

            if key in contact_tags:

                node['contact_number'] = phonenumbers\
                    .format_number(phonenumbers.parse(val, 'US'), phonenumbers.PhoneNumberFormat.NATIONAL)
                continue



            if key in ZIPCODE_TAGS:
                zipcode.add(val)
                continue



            elif address_regex.search(key):
                key = key.replace('addr:', '')
                address[key] = val
                continue



            else:
                node[key] = val

        if len(address) > 0:
            node['address'] = {}
            street_full = None

            for key in address:
                val = address[key]
                if street_regex.search(key):
                    if key == 'street':

                        street_full = audit.clean_street(val)
                else:
                    node['address'][key] = val

            if street_full:
                node['address']['street'] = street_full


        if zipcode:
            node["zipcode"] = list(zipcode)
        return node
    else:
        return None




def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "data/out.json"
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def main():
    data = process_map('data/sample.osm', pretty=False)


if __name__ == '__main__':
    main()





