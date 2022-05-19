import requests
from pprint import pprint

url = "https://xd0u5m6y4r-dsn.algolia.net/1/indexes/event-edition-eve-1515aa4c-c853-40e4-beb1-1315de3e1886_fr-fr/query"

querystring = {"x-algolia-agent":"Algolia^%^20for^%^20vanilla^%^20JavaScript^%^203.27.1","x-algolia-application-id":"XD0U5M6Y4R","x-algolia-api-key":"d5cd7d4ec26134ff4a34d736a7f9ad47"}

payload = {"params": "query=&page=0&facetFilters=&optionalFilters=%5B%5D"}
headers = {
    "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Origin": "https://www.pollutec.com",
    "Referer": "https://www.pollutec.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
    "accept": "application/json",
    "content-type": "application/json",
    "sec-ch-ua": "^\^"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

for x in response.json()['hits']:
    print(x['name'], x['email'], x['phone'])
    #pprint(x['_highlightResult']['companyName']['value'])
