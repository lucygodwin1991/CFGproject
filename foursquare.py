# ------- FOURSQUARE API KEY ------- 

"""
Client ID: 0XFBHJXOKIQBB3FZSJJEGJFHS0WOJI5ZV3ZFDCBCWC2AVLH2
Client SECRET: 2R0RBMTKV3LTRIPR1INR4LFQ2BNPL4FP4GG4AS2F1C4N4ZIO
"""

# ------- Query URL ------- 

https://api.foursquare.com/v2/venues/search?ll=51.504557,-0.017334
&query=bars=browse
&client_id=0XFBHJXOKIQBB3FZSJJEGJFHS0WOJI5ZV3ZFDCBCWC2AVLH2
&client_secret=2R0RBMTKV3LTRIPR1INR4LFQ2BNPL4FP4GG4AS2F1C4N4ZIO
&v=20161024&limit=5&rating 

https://api.foursquare.com/v2/venues/search?ll=51.504557,-0.017334%20
&query=bars=checkin%20
&client_id=0XFBHJXOKIQBB3FZSJJEGJFHS0WOJI5ZV3ZFDCBCWC2AVLH2%20
&client_secret=2R0RBMTKV3LTRIPR1INR4LFQ2BNPL4FP4GG4AS2F1C4N4ZIO%20
&v=20161024&limit=5

# ------- CODE ------- 

import urllib2
import json

url = ('https://api.foursquare.com/v2/venues/search?ll=51.504557,-0.017334%20&query=bars=checkin%20&client_id=0XFBHJXOKIQBB3FZSJJEGJFHS0WOJI5ZV3ZFDCBCWC2AVLH2%20&client_secret=2R0RBMTKV3LTRIPR1INR4LFQ2BNPL4FP4GG4AS2F1C4N4ZIO%20&v=20161024&limit=5')
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

print data['response']
for item in data['response']
print item['name']

