import requests
class DatasetSearch:
    def __init__(self):
        self.url = 'https://www.govdata.de/ckan/api/action/'
        self.action=  "package_search"
        self.title = "?q="
    def titleSearch(self, title):
        self.title=self.title+title
        print(f"Calling the open data portal using package_search action with query parameters. ie: {self.url}")
        self.response = requests.get(f"{self.url+self.action+self.title}&rows=20")
        #print(self.response)
        data = self.response.json()
        #print(f"Success: {data['success']}")
        #print(f"count: {data['result']['count']}")
        #print(f"result length: {len(data['result']['results'])}")
        titles = [ it['title'] for it in data['result']['results'] ]
        #print(titles)
        return titles