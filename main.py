import datetime
import feedparser
import json
import sys

from pymongo import MongoClient

feedJson = 'feed.json'

def loadLinks(fileName):
        assert type(fileName) is str, "Invalid Argument: str expected!"
        print fileName
        try:
                with open(fileName) as fid:
                        feed = json.loads(fid.read())
        except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                sys.exit()
        else:
                return feed

client = MongoClient("192.168.101.5", 27017)
db = client['news_feed']

"""
The
DB --> master --> {'source': , 'feed_title':, 'feed_link_official': , 'feed_link_used', 'feed_published':,
'id':, 'title':, 'link':, 'published':, 'description':}
"""



loadLinks(feedJson)
