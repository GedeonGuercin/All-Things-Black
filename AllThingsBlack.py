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

app.secret_key = 'guercin'


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
    username = auth.authenticate()
    html_code = flask.render_template('index.html',
        username=username)
    response = flask.make_response(html_code)
    return response

#-----------------------------------------------------------------------

@app.route('/profilePage', methods=['GET', 'POST'])
def profilePageTemplate():
    username = auth.authenticate()

    html_code = flask.render_template('profilePage.html',
        username=username)
    response = flask.make_response(html_code)
    return response
	

#-----------------------------------------------------------------------

@app.route('/searchresults', methods=['GET'])
def search_results():
    username = auth().authenticate()

# ----------------------------------------------------------------------

#-----------------------------------------------------------------------

@app.route('/aboutUs', methods=['GET'])
def aboutUsTemplate():
	# username = auth().authenticate()
	# username = username.strip()
	# client_token = generate_client_token()

	# html = flask.render_template(
	# 	'aboutUs.html', username=username)
	html = flask.render_template('aboutUs.html')

	response = make_response(html)
	return response

#-----------------------------------------------------------------------
<<<<<<< Updated upstream
=======
@app.route('/post', methods=['GET'])
def makeaPost():
	title = flask.request.args.get('title')
	post = flask.request.args.get('post')
	print(title)
	print(post)

	html_code = flask.render_template('makeApost.html')
	response = make_response(html_code)
	return response

#-----------------------------------------------------------------------

@app.route('/addpost', methods=['GET'])
def addPost():
	title = flask.request.form.get('title')
	body = flask.request.form.get('body')
	tag = flask.request.form.get('tag')

	database.insertData(title, body, tag)
>>>>>>> Stashed changes

#-----------------------------------------------------------------------

@app.route('/beauty', methods=['GET'])
def beautyTemplate():
	html = flask.render_template('beautypage.html')

	response = make_response(html)
	return response
#-----------------------------------------------------------------------

@app.route('/events', methods=['GET'])
def eventsTemplate():
	html = flask.render_template('eventspage.html')

	response = make_response(html)
	return response
	
#-----------------------------------------------------------------------

@app.route('/food', methods=['GET'])
def foodTemplate():
	html = flask.render_template('foodpage.html')

	response = make_response(html)
	return response
<<<<<<< Updated upstream
=======

#-----------------------------------------------------------------------

@app.route('/addresults', methods=['POST'])
def add_results():
	title = flask.request.form.get('title')
	if (title is None) or (title == ''):
		return 'Enter something'
	body = flask.request.form.get('body')
	if (body is None) or (body == ''):
		return 'Enter something'
	tag = flask.request.form.get('tag')
	if (tag is None) or (tag == ''):
		return 'Enter something'

	print(title)
	print(body)
	print(tag)

	database.addPost(title, body, tag)
	
	return homeTemplate()

#-----------------------------------------------------------------------
@app.route('/delete', methods=['POST'])
def delete_results():
	database.deletePost()
	
	return homeTemplate()
>>>>>>> Stashed changes
