# API : Application Programming Interface

# GET :- Retrieve data
# POST : Write new data
# DELETE : delete junk
# PUT : Update data

# CRUD :
     # Create data - POST
     # Read data - GET
     # Update data - PUT
     # Delete data - DELETE

from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/iseven/<int:n>')
def iseven(n):
    if n%2 == 0:
        result = {
            'Number':n,
            'is Even':True,
            'Server IP': '122.234.213.53'
             }
    else:
        result = {
            'Number':n,
            'is Even':False,
            'Server IP': '122.234.213.53'
             }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
