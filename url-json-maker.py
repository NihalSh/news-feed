import json

news = {'reuters.com' : { 'article': {'top-news': 'http://feeds.reuters.com/reuters/topNews',
                                       'business-news': 'http://feeds.reuters.com/reuters/businessNews',
                                       'world': 'http://feeds.reuters.com/Reuters/worldNews',
                                       'entertainment': 'http://feeds.reuters.com/reuters/entertainment',
                                       'sports': 'http://feeds.reuters.com/reuters/sportsNews',
                                       'technology': 'http://feeds.reuters.com/reuters/technologyNews',
                                       'health': 'http://feeds.reuters.com/reuters/healthNews',
                                       'lifestyle': 'http://feeds.reuters.com/reuters/lifestyle',
                                       'oddly-enough': 'http://feeds.reuters.com/reuters/oddlyEnoughNews'},
                          }
        }
"""        'news.google.com' : {},
        'bbc.com': {},
        'thehindu.com': {}
        }
"""

jsonString = json.dumps(news)

with open('feed.json', 'w') as fid:
        fid.write(jsonString)
