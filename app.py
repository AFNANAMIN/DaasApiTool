# from run import cli
from flask import jsonify
from flask import Flask, render_template , request
app = Flask(__name__)



from DaasApi import DatasetSearch

@app.route("/")
def show_title():
    #user_input = input("Enter the query parameter of ckan search").split(" ")
    #user_input= request.args.get("title")
    sd = DatasetSearch()
    response=sd.titleSearch("title")
    return jsonify(response)

if __name__ == '__main__':
    #show_title()
    app.run(host='0.0.0.0', debug=True)
