#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request, parse

# 快速打印
from util import p


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):  # 不同类型标签有不同的方法
        p('<%s>' % tag)  # 可通过判别标签名取具体值

    def handle_endtag(self, tag):
        p('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        p('<%s/>' % tag)

    def handle_data(self, data):
        p('-------', data)

    def handle_comment(self, data):
        p('<!--', data, '-->')

    def handle_entityref(self, name):
        p('&%s;' % name)

    def handle_charref(self, name):
        p('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


class TestParser(HTMLParser):
    def __init__(self):
        self.time = []
        self.place = []
        self.event = []
        self.__place = False
        self.__event = False

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and len(attrs) and attrs[0][1] == 'event-title':
            self.__place = True
        if tag == 'time':
            self.time.append(attrs[0][1])
        if tag == 'span' and len(attrs) and attrs[0][1] == 'event-location':
            self.__event = True

    def handle_data(self, data):
        if self.__place:
            self.place.append(data)
            self.__place = False
        if self.__event:
            self.event.append(data)
            self.__event = False


parser = TestParser()
with request.urlopen('https://www.python.org/events/python-events/') as resp:
    te = resp.read()
    html = str(te)
    parser.feed(html)

p(parser.time)
p(parser.place)
p(parser.event)


