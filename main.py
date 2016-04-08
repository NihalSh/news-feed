import datetime
import feedparser
import json
import sys
from time import mktime
from datetime import datetime

from pymongo import MongoClient

feedJson = 'feed.json'

def loadLinks(fileName):
        assert type(fileName) is str, "Invalid Argument: str expected!"
        #print fileName
        try:
                with open(fileName) as fid:
                        feed = json.loads(fid.read())
        except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                sys.exit()
        else:
                return feed

def fetchFeeds(feed):
        assert type(feed) is dict, "Invalid Argument: dict expected!"
        for source in feed:
                for news_type in feed[source]:
                        for category in feed[source][news_type]:
                                url = feed[source][news_type][category]

                                doc = {}
                                doc['source'] = source
                                doc['news_type'] = news_type
                                doc['category'] = category
                                
                                d = feedparser.parse(url)
                                doc['feed_title'] = d.feed.title
                                doc['feed_link_official'] = d.feed.link
                                doc['feed_link_used'] = url
                                doc['feed_published'] = datetime.fromtimestamp(mktime(d.feed.published_parsed))

                                for entry in d.entries:
                                        doc['title'] = entry.title
                                        doc['id'] = entry.id
                                        doc['link'] = entry.link
                                        doc['published'] = datetime.fromtimestamp(mktime(entry.published_parsed))
                                        doc['description'] = entry.description
                                """add database functionality here"""
                                print doc
                                break

client = MongoClient("192.168.101.5", 27017)
db = client['news_feed']

"""
The
DB --> master --> {'source': , 'feed_title':, 'feed_link_official': , 'feed_link_used', 'feed_published':,
'id':, 'title':, 'link':, 'published':, 'description':}
"""



feed = loadLinks(feedJson)
fetchFeeds(feed)
