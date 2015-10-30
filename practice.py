import xml.etree.ElementTree as ET

tree = ET.parse('DPR_Basketball_001.xml')
root = tree.getroot()
print("Root: {}".format(root))
print(dir(root))
input("Pause: ")

test = root.findall('{http://www.nycgovparks.org/bigapps/desc/DPR_Basketball_001.txt}facility')
input("Pause: ")
count = 0
for child in test:
    for node in child.iter():
        print("node.tag: {}\nnode.attrib: {}\ntext: {}".format(
                  node.tag, node.attrib, node.text))
        print("\n\n")
    if 'facility' in child.tag:
        count += 1
    print("Count: {}".format(count))
    input()
