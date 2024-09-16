import json
import urllib.request, urllib.parse, urllib.error
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print(f"Retrieving: {url}")
info = json.loads(data)
print(f"Retrieved {len(data)} characters")
comments = info["comments"]
print("Count:", len(comments))
sum = 0
for comment in comments:
    sum += int(comment["count"])
print(f"Sum: {sum}")
