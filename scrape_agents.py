# www.youtube.com/@PropTechFounder

import time
import requests
import json

url = "https://gw.luxurypresence.com/graphql"

offset = 0

payload = json.dumps({
    "query":
    "query Agents($companyId:String, $offset:Int, $limit:Int) { agents(companyId: $companyId, offset: $offset, limit: $limit ) { id firstName lastName position email phoneNumber slug avatar { smallUrl } offices { id name } } }",
    "variables": {
        "companyId": "b26ab618-2b1e-4a17-8868-498b96b52dc0",
        "offset": offset,
        "limit": 100
    }
})
headers = {
    'authority':
    'gw.luxurypresence.com',
    'accept':
    '*/*',
    'accept-language':
    'en-US,en;q=0.9',
    'content-type':
    'application/json',
    'origin':
    'https://serhant.com',
    'referer':
    'https://serhant.com/',
    'sec-ch-ua':
    '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Linux"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'cross-site',
    'user-agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

agents = []

while response.json()["data"]["agents"]:
    offset += 100
    payload = json.dumps({
        "query":
        "query Agents($companyId:String, $offset:Int, $limit:Int) { agents(companyId: $companyId, offset: $offset, limit: $limit ) { id firstName lastName position email phoneNumber slug avatar { smallUrl } offices { id name } } }",
        "variables": {
            "companyId": "b26ab618-2b1e-4a17-8868-498b96b52dc0",
            "offset": offset,
            "limit": 100
        }
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    time.sleep(1)
    agent_data = response.json()["data"]["agents"]
    for agent in agent_data:
        print(agent["firstName"], agent["lastName"], agent["email"],
              agent["phoneNumber"])
    agents.extend(response.json()["data"]["agents"])

response_length = len(response.json()["data"]["agents"])
print(f"Total agents: {offset + response_length}")
