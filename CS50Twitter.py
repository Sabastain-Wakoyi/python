# url = input("URL: ").strip()
#
# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")

import re


url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))

# username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")