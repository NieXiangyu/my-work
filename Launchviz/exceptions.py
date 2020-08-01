# ExceptionCode
LAUNCHVIZ_EXCEPTION     = 0
NODE_DUPLICATION_ERR    = 1
NODE_KIND_ERR           = 2
NODE_NOT_FOUND_ERR      = 3
EDGE_KIND_ERR           = 11
MULTI_LAUNCH_TAG_ERR    = 100
LAUNCH_NO_PACKAGE_ERR   = 101


class LaunchvizException(Exception):
    """Abstract base class for Launchviz exceptions.
    Exceptions with specific codes are specializations of this class."""

    def __init__(self, *args):
        # self.code = LAUNCHVIZ_EXCEPTION
        # TODO: 测试 code
        # self.code = None
        if self.__class__ is LaunchvizException:
            raise RuntimeError(
                "LaunchvizException should not be instantiated directly")
        Exception.__init__(self, *args)

    def _get_code(self):
        return self.code


class NodeDuplicationErr(LaunchvizException):
    code = NODE_DUPLICATION_ERR


class NodeKindErr(LaunchvizException):
    code = NODE_KIND_ERR


class NodeNotFoundErr(LaunchvizException):
    code = NODE_NOT_FOUND_ERR
    POSITION_HEAD = 1
    POSITION_TAIL = 0

    def __init__(self, *args, **kw):
        self.position = kw['position']
        # self.message = kw['message']
        LaunchvizException.__init__(self, args[0])
        # 仅将获得的第一个参数（通常是用于解释/提醒的字符串）传给 Exception 类输出


class EdgeKindErr(LaunchvizException):
    code = EDGE_KIND_ERR


class MultiLaunchTagErr(LaunchvizException):
    code = MULTI_LAUNCH_TAG_ERR


class LaunchNoPackageErr(LaunchvizException):
    code = LAUNCH_NO_PACKAGE_ERR
