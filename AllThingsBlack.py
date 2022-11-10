#!/usr/bin/env python

#-----------------------------------------------------------------------
# AllThingsBlack.py
# Author: Gedeon
#-----------------------------------------------------------------------

import flask
import os
import time
from flask import Flask, render_template, request, make_response, redirect, url_for
from sys import stderr, argv
import database
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

    title = flask.request.args.get('title')

    posts = database.getData(title) # Exception handling omitted                                                                                                                                   

    html_code = flask.render_template('searchresults.html',
        title=title,
        posts=posts)
    response = flask.make_response(html_code)
    return response

# ----------------------------------------------------------------------
@app.route('/home', methods=['GET'])
def homeTemplate():
	html = flask.render_template('home.html')

	response = make_response(html)
	return response

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
@app.route('/post', methods=['GET'])
def makeaPost():
	html_code = flask.render_template('makeApost.html')
	response = make_response(html_code)
	return response

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
