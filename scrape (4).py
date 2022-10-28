import json
import requests, csv

token = ""
org_name = ""
req=org_name + "?fields=posts{comments,likes}"

def req_facebook(req):
  r = requests.get(
    "https://graph.facebook.com/v15.0/"
    + req, {"access_token": token}
  )

  return r

results = req_facebook(req).json()
results = results["posts"]

with open('path/to/csv_file', 'w') as f:
    writer = csv.writer(f)
    count = 0
    data = json.load(results)["data"]

    for row in data:
      if count == 0:
        header = row.keys()
        writer.writerow(header)
        count += 1
        
        writer.writerow(row.values())

    f.close()