import requests

class DatasetSearch:


    url = 'https://www.govdata.de/ckan/api'

    def titleSearch(self, action: str = "package_search",  q: str = None, rows: int = None):
        if action is not None and len(action) != 0:
            self.url = f"{self.url}/action/{action}"

        if q is not None and len(q) != 0:
            self.url = f"{self.url}?q={q}"

        if rows is not None and rows > 0:
            self.url = f"{self.url}&rows={rows}"


        print(f"Calling the open data portal using package_search action with query parameters. ie: {self.url}")
        self.response = requests.get(self.url)
        print(self.response)

        data = self.response.json()
        print(f"Success: {data['success']}")
        print(f"count: {data['result']['count']}")
        print(f"result length: {len(data['result']['results'])}")
        titles = [ it['title'] for it in data['result']['results'] ]
        print(titles)

