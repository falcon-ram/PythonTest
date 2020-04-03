''' Using rapidapi_env venv '''
import requests

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

querystring = {"autoCorrect":"false","pageNumber":"1","pageSize":"10","q":"Taylor Swift","safeSearch":"false"}

headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "f97b719c04msh11b9a010a2e8e58p14e85fjsna8561de07d0a"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# Have to subscribe to the api :(