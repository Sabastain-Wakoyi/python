# import requests
# import sys
#
#
# if len(sys.argv) !=2:
#     sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())


# import json
# import requests
# import sys
#
# name = input("Enter music name: ")
# if len(sys.argv) != 2 or not sys.argv[1]:
# if not name:
#     sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))


# another way of solving the problem above

# import json
# import requests
# import sys
#
# name = "your_music_name"
# if not name:
#     sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + name)
# print(json.dumps(response.json(), indent=2))


#docs.python.org/3/llibrary/json.html

import json
import sys
import requests

if len(sys.argv) !=2 :
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
o = response.json()
for result in 0 ["results"]:
      print(result["trackName"])
