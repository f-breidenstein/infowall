#!/usr/bin/env python

import tornado.websocket
from tornado import gen
import twitterstream
import config

@gen.coroutine
def tweetfeeder():
    client = yield tornado.websocket.websocket_connect(config.WebSocket.url)
    tweetstream = twitterstream.TwitterWallService()
    tweetstream.setCallback(client.write_message)
    tweetstream.listen()

if __name__ == "__main__":
        tornado.ioloop.IOLoop.instance().run_sync(tweetfeeder)
