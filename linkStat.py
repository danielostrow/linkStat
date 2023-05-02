import json
import requests
from tabulate import tabulate

# Load JSON data from file
with open('links.json', 'r') as f:
    data = json.load(f)

# Need a store for the results
results = []

# loop through links in JSON data
for link in data['links']:
    # Send request and get response code
    response = requests.get(link)
    status_code = response.status_code
    
    # Add to result store
    results.append([link, status_code])

# Print store as table
print(tabulate(results, headers=['Link', 'Status']))
