import requests
url= "https://icanhazdadjoke.com/search"

quest=input("Let me tell you a joke! Give me a topic: ")
response= requests.get(url, 
                       headers={"Accept": "application/json"},
                       params={"term":quest, "limit": 1}
                       )

data= response.json()

print(data["results"])