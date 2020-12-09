#https://developers.google.com/docs/api/quickstart/python

import requests
import json
fname = 'Nate'
lname = 'Finney'
url = "https://api.diversitydata.io/?fullname="+fname+"%20"+lname
response = requests.get(url)
print (response.text)
data = json.loads(response.text)
# JSON in python is designed to convert data from APIs
print (data["fullname"])