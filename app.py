# from run import cli

from DaasApi import DatasetSearch

if __name__ == "__main__":
    user_input = input("Enter the query parameter of ckan search  ").split(" ")
    sd = DatasetSearch()
    sd.titleSearch(user_input[0])
