from flask import Flask, render_template, json, request
from flaskext.mysql  import MySQL
from werkzeug import generate_password_hash, check_password_hash
import json, time, pprint
import requests
from json import JSONEncoder
from urllib.request import Request, urlopen

app = Flask(__name__)

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'welcome1'
app.config['MYSQL_DATABASE_DB'] = 'fitbank'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

custom_fetch = lambda method, relative_url, body=None: json.loads(urlopen(Request(base_url+relative_url, data=json.dumps(body).encode('utf8'), method=method, headers={'Content-Type': 'application/json', 'Authorization': 'API-Key ' + api_key, 'Accept': 'application/json'})).read().decode('utf-8')); post = lambda url, body=None: custom_fetch("POST", url, body); get = lambda url: custom_fetch("GET", url); put = lambda url, body=None: custom_fetch("PUT", url, body)

base_url = 'https://play.railsbank.com/'
endpoint = 'v1/customer/endusers'
api_key = 'wuEG2bgIWdIHpz0ycJCVAnf5hSPBRYCJ#W4CKzKNEyMxHtcMKRXWWWzc1mT8l881YUjxEvDktENRRuufBsMfNVL43zHTbGTa9'

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/loadMain', methods=['POST','GET'])
def loadMain():

    _email = request.form['inputName']
    _password = request.form['inputAddress']
    
    print(_email)
    return render_template('main.html')

@app.route('/createEndUser')
def showSignUp():
    return render_template('signup.html')

def signUp():
    print('hello world')

    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _inputPostCode = request.form['inputPostCode']
    _inputCity = request.form['inputCity']
    _inputCountry = request.form['inputCountry']
    response = post(endpoint,{'person': {'name': _name,'email': _email,'address': {'address_postal_code': _inputPostCode,'address_city': _inputCity,'address_iso_country': _inputCountry}}})


    pprint.pprint(response)
    enduser_id = response['enduser_id']
    print(enduser_id)
    # validate the received values
    #  if _name and _email and _password: hel


    # All Good, let's call MySQL

    #            conn = mysql.connect()
    #           cursor = conn.cursor()
    #          _hashed_password = generate_password_hash(_password)
    #         cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
    #        data = cursor.fetchall()

    #            if len(data) is 0:
    #               conn.commit()
    #              return json.dumps({'message': 'User created successfully !'})
    #         else:
    #            return json.dumps({'error': str(data[0])})
    #   else:
    #      return json.dumps({'html': '<span>Enter the required fields</span>'})
    return render_template('main.html')

if __name__ == "__main__":
    app.run()
