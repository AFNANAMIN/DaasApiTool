# from run import cli
from flask import jsonify
from flask import Flask, render_template , request
app = Flask(__name__)



from DaasApi import DatasetSearch

@app.route("/")
def show_title():
    #user_input = input("Enter the query parameter of ckan search").split(" ")
    #http://192.168.10.6:5000/?title=luftbild
    user_input= request.args.get("title") if "title" in  request.args.keys() else ""
    sd = DatasetSearch()
    response=sd.titleSearch(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
