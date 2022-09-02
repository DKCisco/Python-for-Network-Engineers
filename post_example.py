import json
import httpx
from rich import print as rprint

headers = { 
    'Authorization': 'Bearer 2fd5a2286521951c3941fd74d72ed4fff643c9eb4924a9d22da81fe4c02c61b1',
}

my_url = "https://gorest.co.in/public/v2/users"

payload = {
    "name":"Bob Smith", 
    "gender":"male", 
    "email":"bob.smith11@15ce.com", 
    "status":"active"
}

def post_stuff(url):
    with httpx.Client() as client:
        response = client.post(url, headers=headers, data=payload)
        structured_response = json.loads(response.text)
        return response, structured_response

results = post_stuff(url=my_url)
rprint(results)