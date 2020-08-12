from xml.dom import Node as domNode
from xml.dom import minidom as xml_dom

point = './launch/pointcloud_to_laserscan.launch'
navigation = './launch/navigation_real.launch'
hunter = './launch/hunter_tf.launch'
nav_bt = './launch/navigation_bt.launch'
rs232 = './launch/rs232_driver.launch'

tags0 = xml_dom.parse('./launch/path_follower.launch').getElementsByTagName('launch')[0].childNodes
tags1 = xml_dom.parse(point).getElementsByTagName('launch')[0].childNodes
tags2 = xml_dom.parse(navigation).getElementsByTagName('launch')[0].childNodes
tags3 = xml_dom.parse(hunter).getElementsByTagName('launch')[0].childNodes
tags4 = xml_dom.parse(nav_bt).getElementsByTagName('launch')[0].childNodes
tags5 = xml_dom.parse(rs232).getElementsByTagName('launch')[0].childNodes

def make_context(tags: list, context: dict):
    '''
    将传入参数context这一字典根据标签列表tags生成，该函数只处理tagName为'arg'与'anon'的元素并记录到context中
    @param tags: 用于生成菜单context的标签列表
    @param context: 这个参数会改变，该字典会根据tags补充完成
    '''

    for tag in [t for t in tags if t.nodeType == domNode.ELEMENT_NODE]:
        '''
        if t.nodeType == domNode.ELEMENT_NODE为去掉注释
        xml.dom.Node=domNode，
        t为标签列表tags中满足t.nodeType == domNode.ELEMENT_NODE的标签，ELEMENT_NODE是一个枚举值，代表元素节点类型。
        每次循环中tag为标签列表tags中满足这个条件的标签
        '''
        if tag.tagName == 'arg':
            if 'arg' not in context.keys():
                context['arg'] = {}
            # 第一次'arg'不在context.keys()中就先加入作为key的一个，value暂时为空

            name = tag.attributes._attrs['name'].nodeValue
            # 若上个文件中已经设置了此参数值，则不再读取此函数中参数值
            '''
            nodeValue 属性设置或返回节点的值，根据其类型。为xml.dom.minidom中内容
            访问元素属性：Node.attributes[“id”]
            a.name:就是上面的 “id”， a.value:属性的值
            '''
            try:
                value = tag.attributes._attrs['value'].nodeValue
            except KeyError:
                if name in context['arg'].keys():
                    value = context['arg'][name]
                else:
                    try:
                        value = tag.attributes._attrs['default'].nodeValue
                    except KeyError as ex:
                        #self.recorder.add_arg(arg_name=name, tag=tag, file=self.file)
                        pass
            context['arg'][name] = value

            '''
            用value变量记录属性'value'的值，不存在则用value记录菜单context中arg名（如果有）
            如果还是没有，value记录属性'default'值，还是没有就向recorder中记录name与标签tag
            最后菜单context中'arg'参数名记为value
            '''

        elif tag.tagName == 'anon':
            if 'anon' not in context.keys():
                context['anon'] = {}
            if name not in context['anon'].keys():
                name = tag.attributes._attrs['name'].nodeValue
                value = tag.attributes._attrs['default'].nodeValue
                context['anon'][name] = value
        '''
        标签名为anon处理与上面标签名arg类似，第一次不在就加入目录context的keys()中，
        name不在'anon的keys()中就把属性'name'的节点赋值给name，默认'default'节点赋值给value
        最后补充菜单context的'anon'目录
        '''
    return context

context0={}
context1=make_context(tags0, context0)
print(context1)