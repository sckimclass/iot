from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/method', methods=['GET'])
def method():
    if request.method == 'GET':
        id = request.args["id"]
        password = request.args.get("password")
        return "data ({}, {})".format(id, password)
    
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
