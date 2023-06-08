# import requests
# import sys
#
#
# if len(sys.argv) !=2:
#     sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())

import json
import requests
import sys

if len(sys.argv) != 2 or not sys.argv[1]:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json()))

#docs.python.org/3/llibrary/json.html
