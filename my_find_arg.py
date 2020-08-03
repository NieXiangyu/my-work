from xml.dom import minidom as xml_dom

def my_find_args(file_in: str, file_out: str):
    #@param file_in： 带有完整路径的文件名，是要分析的输入文件
    #@param file_out: 将结果输出到该文件中
    f = open(file_out, "w")
    command_list = ['$(arg ', '$(env ', '$(optenv ', '$(anon ', '(find ', '(eval ']
    tags = xml_dom.parse(file_in).getElementsByTagName('launch')
    if tags and len(tags) == 1:
        arglist=tags[0].getElementsByTagName('arg')