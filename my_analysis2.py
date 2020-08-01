import xml.etree.ElementTree as ET
tree=ET.ElementTree('D:\\我的文档\\GitHub\\my-work\\amcl.launch')
print(tree)
root=tree.getroot()
print(root)
#print(root.attrib)
for child in root:
   print(child.attrib)