import json

news = {'reuters.com' : { 'article': {'top-news': 'http://feeds.reuters.com/reuters/topNews',
                                       'business-news': 'http://feeds.reuters.com/reuters/businessNews',
                                       'world': 'http://feeds.reuters.com/Reuters/worldNews',
                                       'entertainment': 'http://feeds.reuters.com/reuters/entertainment',
                                       'sports': 'http://feeds.reuters.com/reuters/sportsNews',
                                       'technology': 'http://feeds.reuters.com/reuters/technologyNews',
                                       'health': 'http://feeds.reuters.com/reuters/healthNews',
                                       'lifestyle': 'http://feeds.reuters.com/reuters/lifestyle',
                                       'oddly-enough': 'http://feeds.reuters.com/reuters/oddlyEnoughNews'
                                      },
                          'video': {'breaking-news': 'http://feeds.reuters.com/reuters/USVideoBreakingviews',
                                    'technology-news': 'http://feeds.reuters.com/reuters/USVideoTechnology',
                                    'business-news': 'http://feeds.reuters.com/reuters/USVideoBusiness',
                                    'lifestyle': 'http://feeds.reuters.com/reuters/USVideoLifestyle'
                                    }
                          },
        'bbc.com': {'article': {'top-stories': 'http://feeds.bbci.co.uk/news/rss.xml',
                                'world': 'http://feeds.bbci.co.uk/news/world/rss.xml',
                                'business': 'http://feeds.bbci.co.uk/news/business/rss.xml',
                                'politics': 'http://feeds.bbci.co.uk/news/politics/rss.xml',
                                'technology': 'http://feeds.bbci.co.uk/news/technology/rss.xml'
                                },
                    'video': {'top-stories': 'http://feeds.bbci.co.uk/news/video_and_audio/news_front_page/rss.xml?edition=uk',
                              'world': 'http://feeds.bbci.co.uk/news/video_and_audio/world/rss.xml',
                              'business': 'http://feeds.bbci.co.uk/news/video_and_audio/business/rss.xml',
                              'politics': 'http://feeds.bbci.co.uk/news/video_and_audio/politics/rss.xml',
                              'technology': 'http://feeds.bbci.co.uk/news/video_and_audio/technology/rss.xml'} 
                    }
        
        }

jsonString = json.dumps(news)

with open('feed.json', 'w') as fid:
        fid.write(jsonString)
