"""有些REST API 会把参数放到URL中，比如Github的API：
GET/users/:user/repos,调用时，需要把：user替换为实际
用户名。如果我们能写出这样的链式调用：
               Chain.users('michael').repos"""


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, name):
        return Chain('%s/%s' % (self._path, name))

    def __str__(self):
        return self._path


print(Chain().users('michael').repos)
