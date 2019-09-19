from typing import Optional, Awaitable

import tornado.ioloop
from tornado.web import RequestHandler, Application
from tornado.options import define, parse_command_line, options


define('port', default=8001, type=int)

class MainHandler(RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.write('hello word')


def create_app():

    return Application(handlers=[
        (r'/', MainHandler),
    ])


if __name__ == '__main__':

    # 解析启动命令
    parse_command_line()

    app = create_app()

    app.listen(options.port)

    tornado.ioloop.IOLoop.current().start()