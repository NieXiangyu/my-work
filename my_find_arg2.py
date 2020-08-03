import xml.etree.ElementTree as ET

def my_find_arg(filein, fileout):
    '''
   @param filein: 带有完整路径的文件名，是要分析的输入文件
   @param fileout: 将结果输出到该文件中
   该函数将所有元素（不管是在什么层次）以及属性全部遍历，找出带有'$'字符部分后输出对应的元素，属性与属性具体内容
   '''
    f=open(fileout,"w")
    tree=ET.parse(filein)
    root=tree.getroot()
    arg_list = ['$(arg ', '$(env ', '$(optenv ', '$(anon ', '(find ', '(eval ']
    tag_list = ['launch', 'node', 'machine', 'include', 'remap', 'env', 'param', 'rosparam', 'group', 'test', 'arg']
    for tag in tag_list:
        for ele in root.iter(tag):
            for key, value in ele.attrib.items():
                if '$' in value:
                    line='<'+tag+' '+key+'='+value+'/>'+'\n'
                    f.writelines(line)
    f.close()

my_find_arg("hybrid_a_star.launch", 'result3.txt')


