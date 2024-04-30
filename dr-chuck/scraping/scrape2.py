# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:

    url = input("Enter URL: ")
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    count = int(input("Enter count: "))
    position = int(input("Enter position: ")) - 1
    print(f"Retrieving: {url}")
    # Retrieve all of the anchor tags
    tags = soup("a")
    i = 1
    tag = tags[position]
    url = tag.get("href", None)
    print(f"Retrieving: {url}")

    while i < count:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup("a")
        tag = tags[position]
        url = tag.get("href", None)
        print(f"Retrieving: {url}")
        i += 1

except:
    print("An exception occurred")
