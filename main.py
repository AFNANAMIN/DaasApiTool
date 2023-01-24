# from run import cli

from daas import DatasetSearch

if __name__ == "__main__":
    user_input = input("enter action and search query: ").split(" ")
    sd = DatasetSearch()
    sd.titleSearch(user_input[0],
                   user_input[1] if len(user_input) > 1 else None,
                   int(user_input[2]) if len(user_input) > 2 else None )
