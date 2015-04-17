import twitter
import json

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'p7HUdPLlkKaqlPn6TzKkA'
CONSUMER_SECRET = 'R7I1LRuLY27EKjzulutov74lKB0FjqcI2DYRUmsu7DQ'
OAUTH_TOKEN = '14898655-TE9dXQLrzrNd0Zwf4zhK7koR5Ahqt40Ftt35Y2qY'
OAUTH_TOKEN_SECRET = 'q1lSRDOguxQrfgeWWSJgnMHsO67bqTd5dTElBsyTM'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = '#TOP GEAR #BBC'

count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    print("Length of statuses", len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
    except KeyError:
        pass
    # except KeyError, e:
    #     pass

twitter_result = []

# Show one sample search result by slicing the list...
#print json.dumps(statuses[0]['created_at'], statuses[0]['created_at'], indent=1)

status_texts = [ status['text']
                 for status in statuses ]

status_created = [ status['created_at']
                 for status in statuses ]


# Explore the first 5 items for each...

print(json.dumps(status_texts[0:200] + status_created[0:200], indent=1))