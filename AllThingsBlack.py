#!/usr/bin/env python

#-----------------------------------------------------------------------
# AllThingsBlack.py
# Author: Gedeon
#-----------------------------------------------------------------------

import flask
import os
import time
from flask import Flask, request, make_response, redirect, url_for

import auth

#-----------------------------------------------------------------------


app = flask.Flask(__name__, template_folder='.')

#app.secret_key = os.environ['APP_SECRET_KEY']


#-----------------------------------------------------------------------
# Routes for authentication.

@app.route('/logoutapp', methods=['GET'])
def logoutapp():
    return auth.logoutapp()

@app.route('/logoutcas', methods=['GET'])
def logoutcas():
    return auth.logoutcas()

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html_code = flask.render_template('index.html')
    response = flask.make_response(html_code)
    return response

#-----------------------------------------------------------------------

@app.route('/profilePage', methods=['GET', 'POST'])
def profilePageTemplate():
	#username = auth().authenticate()
	html_code = flask.render_template('profilePage.html')
	#username = username.strip()
	#classYear = request.args.get('classYear')
	#major= request.args.get('major')
	response = flask.make_response(html_code)
	return response
	

#-----------------------------------------------------------------------

@app.route('/searchresults', methods=['GET'])
def search_results():
    username = auth().authenticate()

# ----------------------------------------------------------------------

@app.route('/aboutUs', methods=['GET'])
def aboutUsTemplate():
	username = auth().authenticate()
	username = username.strip()
	# client_token = generate_client_token()

	html = render_template(
		'aboutUs.html', username=username)

	response = make_response(html)
	return response

#-----------------------------------------------------------------------