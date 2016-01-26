class OAuth:
    username = "my_twitter_username"
    consumer_key = "get this from your twitter app foo"
    consumer_secret = "get this from your twitter app foo"
    credfile = "~/.my_twitterapp_credentials"

class WebSocket:
    url = "ws://localhost:8999/ws"
    port = 8999

class TwitterStream:
    timeout = 10
    block = False
    heartbeat_timeout = 90
    keywords = [["linux","debian","arch"],["32c3"]]
