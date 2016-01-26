# infowall


Twitterwall using websockets.
This is only some playing with tornado, websockets and the twitter streaming API

**Attention**  
Don't use this code in production. It is not safe and contains for sure a xss vulnerability.


### Requirements

  * Create an app to have access to the API over here: https://apps.twitter.com/
  * Python 3
  * tornado
  * twitter

### Quickstart
  * copy example.config.py to config.py
  * edit config.py
  * edit html/config.js
  * python tornado_server.py
  * python tornado_twitter.py
  * open a browser (with websockets enabled) an navigate to the target dir (file://foobar/infowall/html/index.html or so)
  * python tornado_client.py (cli to send messages to different/new channels on the wall)
