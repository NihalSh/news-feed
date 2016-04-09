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
                                try:
                                        doc['feed_published'] = datetime.fromtimestamp(mktime(d.feed.published_parsed))
                                except:
                                        print url
                                        doc['feed_published'] = ''

                                for entry in d.entries:
                                        try:
                                                doc['title'] = entry.title
                                                doc['id'] = entry.id
                                                doc['link'] = entry.link
                                                doc['published'] = datetime.fromtimestamp(mktime(entry.published_parsed))
                                                doc['description'] = entry.description
                                                """add database functionality here"""
                                        except:
                                                print "entry faulty: not added to database"
                                        else:
                                                if addToDatabase(doc.copy()) == True:
                                                        print "Entry added to or already present in DB"
                                                else:
                                                        print "Database error!"
                                                

def addToDatabase(doc):
        try:
                client = MongoClient("192.168.101.5", 27017)
                db = client['news_feed']
                collection = db['master']
                assert type(doc) is dict, "Invalid Argument: dict expected!"
                if collection.find_one({'id': doc['id']}) is None:
                        result = collection.insert_one(doc)
                        print result.inserted_id
                        return result.acknowledged
                else:
                        print "skipped"
                        return True
        except:
                return False

"""
The
DB --> master --> {'source': , 'feed_title':, 'feed_link_official': , 'feed_link_used', 'feed_published':,
'id':, 'title':, 'link':, 'published':, 'description':}
"""

feed = loadLinks(feedJson)
fetchFeeds(feed)
