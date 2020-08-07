import xml.etree.ElementTree as ET

def find_arg_attr(filein, fileout):
   #@param filein: 带有完整路径的文件名，是要分析的输入文件
   #@param fileout: 将结果输出到该文件中
    f=open(fileout,"w")
    tree=ET.parse(filein)
    root=tree.getroot()
    for arg in root.iter('arg'):
        try:
            line= arg.attrib['name']+'='+arg.attrib['default']+'\n'
            f.writelines(line)
        except KeyError:
            pass
    f.close()

find_arg_attr('D:\\我的文档\\GitHub\\my-work\\amcl.launch','result2.txt')


