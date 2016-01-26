#!/usr/bin/env python

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import config

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        WSHandler.clients.append(self)

    def on_message(self, message):
        for client in self.clients:
            # FIXME: This is just a message hub. Perhaps it should not just pass
            # what it gets, but do some checking on xss foo, etc.
            client.write_message(message)

    def on_close(self):
        WSHandler.clients.remove(self)

    def check_origin(self, origin):
        # FIXME: This is a hack to bypass 403 errors.
        return True


application = tornado.web.Application([(r'/', WSHandler),])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(config.WebSocket.port)
    tornado.ioloop.IOLoop.instance().start()
