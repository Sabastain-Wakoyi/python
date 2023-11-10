# url = input("URL: ").strip()
#
# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")

import re

url = input("URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"Username: {username}")