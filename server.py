from flask import Flask, request, jsonify, send_file
import os as os
import csv
from pymysql import *
import pandas.io.sql as sql
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/register',methods=['POST'])
def register():
	uid = request.form['uid']
	name = request.form['name']
	print("uid : ",uid)
	print("name : ",name)
	con=connect(user="b62fd86f8ddd49",password="49c109c9",host="us-cdbr-east-02.cleardb.com",database="heroku_27300199120befc")
	x = "insert into test_table (name, id) values ("+str(name)+","+str(uid)+"); "
	cursor = con.cursor()
	cursor.execute(x)
	con.commit()
	cursor.close()
	return("Updated")

@app.route('/show',methods=['GET'])
def show():
	uid = request.form['uid']
	con=connect(user="b62fd86f8ddd49",password="49c109c9",host="us-cdbr-east-02.cleardb.com",database="heroku_27300199120befc")
	x = "select * from test_table where id = "+uid+";"
	cursor = con.cursor()
	cursor.execute(x)
	con.commit()
	cursor.close()
	return("Show")

@app.route('/react_post',methods=['POST'])
def react_post():
	data = request.json
	print(data)
	return("Got data !")

@app.route('/post',methods=['POST'])
def post():
	details = request.json
	uname = json.dumps(details["name"])
	uid = json.dumps(details["id"])
	con=connect(user="b62fd86f8ddd49",password="49c109c9",host="us-cdbr-east-02.cleardb.com",database="heroku_27300199120befc")
	x = "insert into test_table (name, id) values ("+str(uname)+","+str(uid)+"); "
	cursor = con.cursor()
	cursor.execute(x)
	con.commit()
	cursor.close()
	print(uname)
	print(uid)
	return("Updated",details)

@app.route('/show_db',methods=['POST'])
def show_db():
	details = request.json
	uid = json.dumps(details["id"])	
	print("details : ",details)
	print(uid)
	con=connect(user="b62fd86f8ddd49",password="49c109c9",host="us-cdbr-east-02.cleardb.com",database="heroku_27300199120befc")
	cur = con.cursor()
	cur.execute("select * from test_table where id = "+str(uid)+";")
	# row_headers=[x[0] for x in cur.description] #this will extract row headers
	rv = cur.fetchall()
	# json_data=[]
	# for result in rv:
	# 	json_data.append(dict(zip(row_headers,result)))
	# print(rv)
	total = json.dumps(rv)
	print(total)
	# con.commit()
	# cursor.close()
	return(total)

	# return(requests.Response(y))

if __name__ == "__main__":
	app.run(port=8000)