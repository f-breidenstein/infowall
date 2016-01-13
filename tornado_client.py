#!/usr/bin/env python

import tornado.websocket
from tornado import gen
import json
import config




@gen.coroutine
def test_ws():
    client = yield tornado.websocket.websocket_connect(config.WebSocket.url)
    msg = ""
    while True:
        msg = input("-> ")
        if msg:
            tweet = { "user":
                        { "screen_name": config.Client.nick,
                          "name": config.Client.name
                        },
                      "entities":"",
                      "channel":input("channel "),
                      "text": msg }

            #client.send(json.dumps(tweet))
            client.write_message(json.dumps(tweet))
            if msg == "quit":
                client.close()
        message = yield client.read_message()
        print( message )

if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().run_sync(test_ws)
