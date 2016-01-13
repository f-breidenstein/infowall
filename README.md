infowall
========

Twitterwall using websockets.

!! Attention !!

Don't use this code in production. Is is not safe and contains for sure a xss vulnerability.

This is only some playing with tornado websockets and the twitter streaming api

Requirements:
  python3 modules
  * tornado
  * twitter

Quickstart:
  * clone the repo
  * edit config.py
  * edit html/config.js
  * python tornado_server.py
  * python tornado_twitter.py
  * open a browser (with websockets enabled) an navigate to the target dir (file://foobar/infowall/html/index.html or so)

