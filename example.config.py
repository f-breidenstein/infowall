# Parameters for the OAuth stuff
class OAuth:
    # twitter username
    username = "my_twitter_username"
    consumer_key = "get this from your twitter app foo"
    consumer_secret = "get this from your twitter app foo"
    # the credfile will be written if not exists.
    credfile = "~/.my_twitterapp_credentials"

class WebSocket:
    url = "ws://localhost:8999/ws"
    port = 8999


# Configuration for the TwitterStream.
class TwitterStream:
    # if no tweets have been received within a timeout period, a timeout will
    # be triggerd. This parameter is only used if "block" is set to "False".
    timeout = 10

    # block tells if the connection is blocking or not.
    # when blocking, the "timeout" parameter will not be recognized.
    # if set to False, the timeout will trigger if not tweet have been
    # received. Afterwards, the loop will continue to wait for and process
    # tweets. timeout and block will be usefull in future when there is a
    # possibility in place to pass a function to the mainloop.
    block = False

    # a heartbeat_timeout will force the connection to close.
    # this parameter configures the client side timeout for connection
    # heartbeats.
    heartbeat_timeout = 90

    # keywords is a list of lists with keywords. Each entry in the keywords
    # list must be a list. Each of those lists contains the words to filter
    # for. For each list in keywords the channel attribute of the tweet will
    # be filled and a column for the channel will be added to the wall.
    keywords = [["linux","debian","arch"],["32c3"]]

class Client:
    nick = "testcick"
    name = "Test Nick"
    channel = "test_channel"
