from xml.dom import Node as domNode
from xml.dom import minidom as xml_dom


tags = xml_dom.parse('D:\\我的文档\\GitHub\\my-work\\amcl.launch').getElementsByTagName('launch')[0].childNodes
print(tags)
for tag in [t for t in tags]:
    print(tag)
    #print(tag.tagName)
    #print(tag.attribute)


'''
def find_arg_attr(file_in: str, file_out: str)

    @param file_in： 带有完整路径的文件名，是要分析的输入文件
    @param file_out: 将结果输出到该文件中

     tags = xml_dom.parse(file_in).getElementsByTagName('launch')
    #print(tags)
     for ele in tags 
         if ele == 'arg'
            


     f = open(file_out, "w")
      
find_arg_attr('amcl.launch', 'result1.txt')
'''