import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    parms = dict()
    parms["address"] = address
    url = address
    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print("Retrieved", len(data), "characters")
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall(".//count")
    sum = 0
    for res in results:
        sum += int(res.text)
    print(sum)
