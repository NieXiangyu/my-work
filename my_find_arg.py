import xml.sax

'''
找出$(arg 参数并还原为默认值
该程序查找了arg定义所在行号与$(arg 出现语句所在行号。
此处行号从<launch>开始算第一行，且无视空行，每读一个元素增加一行
要得到文本中的行号（直观上看上去的），直接f.readlines(),f.writelines()计数，
但是这样体现不出xml文件结构特点，是否有需求之后考虑
'''
class LaunchHandler(xml.sax.ContentHandler):
    def __init__(self, file_out):
        self.CurrentTag = ""
        self.arg_list = {}
        self.Currentline = 0
        self.file=file_out


    def startDocument(self):
        self.f=open(self.file,"w")

    # 元素开始事件处理
    #行号从<launch>开始算第一行
    def startElement(self, tag, attr):
        self.CurrentTag = tag
        self.Currentline = self.Currentline+1
        if tag == 'arg' and 'default' in attr.keys():
            self.arg_list[attr['name']]=(attr['default'], self.Currentline)
        for ele in attr.values():
            if '$(arg ' in ele:
                line='<'+tag+' '
                for key, value in attr.items():
                    if '$(arg' in value:
                        nvalue1=value[value.find('$')+6: value.find(')')]
                        nvalue2=self.arg_list[nvalue1][0]
                        line = line + key + '="' + nvalue2 + '"'
                    else:
                        line = line + key + '="' + value + '" '
                line=line + '/>' + '(' + nvalue1 + '->' + nvalue2 + ')' + 'define: line:' + str(self.arg_list[nvalue1][1]) + '\n'
                line='line:' + str(self.Currentline) + ': ' +line
                self.f.writelines(line)

    def endDocument(self):
        self.f.close()


    # 创建一个 XMLReader
parser = xml.sax.make_parser()
    # turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
Handler = LaunchHandler('result4.txt')
parser.setContentHandler(Handler)
parser.parse("hybrid_a_star.launch")
