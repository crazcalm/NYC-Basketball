import xml.etree.ElementTree as ET

from collections import namedtuple
import json


Court = namedtuple("basketball_court", "name location num_of_courts accessible longitude latitude")

tree = ET.parse('DPR_Basketball_001.xml')
root = tree.getroot()
print("Root: {}".format(root))
print(dir(root))
input("Pause: ")

test = root.findall('{http://www.nycgovparks.org/bigapps/desc/DPR_Basketball_001.txt}facility')
input("Pause: ")
count = 0

data = []
for child in test:

    name = ""
    location = ""
    num_of_courts = ""
    accessible = ""
    latitude = ""
    longitude = ""

    for node in child.iter():
        print("node.tag: {}\nnode.attrib: {}\ntext: {}".format(
                  node.tag, node.attrib, node.text))
        print("\n\n")

        if "Name" in node.tag:
            name = node.text

        elif "Location" in node.tag:
            location = node.text

        elif "Num_of_Courts" in node.tag:
            num_of_courts = node.text

        elif "Accessible" in node.tag:
            accessible = node.text

        elif "lat" in node.tag:
            latitude = node.text

        elif "lon" in node.tag:
            longitude = node.text

    if 'facility' in child.tag:
        count += 1

    tempt = Court(name=name, location=location, num_of_courts=num_of_courts,
                  accessible=accessible, latitude=latitude, longitude=longitude)

    # Turns the numedtuple to a json object
    json_ = json.dumps(tempt.__dict__)

    print("tempt: ", tempt)
    print("\njson: ", json_)

    data.append(tempt)

    print("Count: {}".format(count))
    input()
