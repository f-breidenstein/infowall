#!/usr/bin/env python
import json
import os
from twitter import *
from twitter.util import printNicely
import config
import re

Timeout = {'timeout': True}
Hangup = {'hangup': True}
DecodeError = {'hangup': True, 'decode_error': True}
HeartbeatTimeout = {'hangup': True, 'heartbeat_timeout': True}

class TwitterWallService:
    def __init__(self):

        # OAuth stuff
        self.creds = os.path.expanduser(config.OAuth.credfile)
        self.oauth_token = ""
        self.oauth_secret = ""
        self.auth = None
        if not os.path.exists(self.creds):
            oauth_dance(
    		config.OAuth.username,
                config.OAuth.consumer_key,
                config.OAuth.consumer_secret,
                self.creds)

        (self.oauth_token, self.oauth_secret) = read_token_file(self.creds)
        self.auth = OAuth(
            self.oauth_token,
            self.oauth_secret,
            config.OAuth.consumer_key,
            config.OAuth.consumer_secret)


        self.keywords = None
        self.filterstr = None
        self.setKeywords(config.TwitterStream.keywords)
        self.callback = None
        self.stream = None
        self.stream_args = dict(
            timeout=config.TwitterStream.timeout,
            block=config.TwitterStream.block,
            heartbeat_timeout=config.TwitterStream.heartbeat_timeout)
        self.query_args = dict()

    def setKeywords(self, keywords):
        self.keywords = keywords
        self.filterstr = ""
        for words in self.keywords:
            if len(self.filterstr) > 0:
                self.filterstr += ","
            self.filterstr += ",".join(words)

        print (self.filterstr)
        self.query_args = dict()
        if self.filterstr:
            # https://dev.twitter.com/docs/streaming-apis/parameters#track
            self.query_args['track'] = self.filterstr

    def listen(self):
        self.stream = TwitterStream(auth=self.auth, **self.stream_args)

        self.query_args = dict()
        if self.filterstr:
            # https://dev.twitter.com/docs/streaming-apis/parameters#track
            self.query_args['track'] = self.filterstr

        if self.filterstr:
            self.tweet_iter = self.stream.statuses.filter(**self.query_args)
        else:
            self.tweet_iter = self.stream.statuses.sample()
        for tweet in self.tweet_iter:
            if tweet is None:
                 printNicely("-- None --")
            elif tweet is Timeout:
                printNicely("-- Timeout --")
            elif tweet is HeartbeatTimeout:
                printNicely("-- Heartbeat Timeout --")
            elif tweet is Hangup:
                printNicely("-- Hangup --")
            elif tweet.get('text'):
                if self.callback:
                    # We parse the text to sort tweet into right channel
                    for keywords in self.keywords:
                        for word in keywords:
                            r = re.search(word,tweet.get("text"),re.IGNORECASE)
                            if not r:
                                continue
                            else:
                                tweet["channel"] = "," .join(keywords)
                                self.callback(json.dumps(tweet))
            else:
                printNicely("-- Some data: " + str(tweet))

    def setCallback(self,callback_function=None):
        if callback_function:
            self.callback = callback_function

