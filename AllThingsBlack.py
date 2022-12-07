#!/usr/bin/env python

#-----------------------------------------------------------------------
# AllThingsBlack.py
# Author: Gedeon
#-----------------------------------------------------------------------

import flask
# import flask_wtf.csrf
import os
import time
from flask import Flask, render_template, request, make_response, redirect, url_for
from sys import stderr, argv
import database
import auth
import auth_admin

#-----------------------------------------------------------------------


app = flask.Flask(__name__, template_folder='.')

app.secret_key = 'guercin'

# flask_wtf.csrf.CSRFProtect(app)
#-----------------------------------------------------------------------
# Routes for authentication.

@app.route('/adminlogout', methods=['GET'])
def adminlogout():
    return auth_admin.logout()

@app.route('/adminlogin', methods=['GET'])
def adminlogin():
    return auth_admin.login()

@app.route('/handlelogin', methods=['POST'])
def handle_login():
    return auth_admin.handle_login()

@app.route('/logoutapp', methods=['GET'])
def logoutapp():
    return auth.logoutapp()

@app.route('/logoutcas', methods=['GET'])
def logoutcas():
    return auth.logoutcas()

#-----------------------------------------------------------------------

app.before_request
def before_request():
	if not flask.request.is_secure:
		url = flask.request.url.replace('http://', 'https://', 1)
		return flask.redirect(url, code=301)
	return None

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	# username = auth.authenticate()
	# print(username)
	html_code = flask.render_template('index.html')
	response = flask.make_response(html_code)
	return response

#-----------------------------------------------------------------------

# @app.route('/profilePage', methods=['GET', 'POST'])
# def profilePageTemplate():
#     # username = auth.authenticate()

#     html_code = flask.render_template('profilePage.html')
#     response = flask.make_response(html_code)
#     return response
	

# #-----------------------------------------------------------------------

@app.route('/delete', methods=['GET'])
def delete():
	username = auth_admin.authenticate()
	posts =  database.getData(True)

	html_code = flask.render_template('delete.html', username=username, posts=posts)
	response = flask.make_response(html_code)
	return response
	

#-----------------------------------------------------------------------

@app.route('/deleteresults', methods=['POST'])
def deleteresult():
	username = auth_admin.authenticate()
	title  = flask.request.form.get('title')
	# if (title is None) or (title.strip() == ''):
	# 	return report_results('Missing ISBN', '')
	title = title.strip()
	database.delete_post(title)

	message1 = 'The deletion done by ' + username+ ' was successful'
	message2 = 'The database now does not contain a book with Title '
	message2 += title

	return report_results(username, message1, message2)
	

#-----------------------------------------------------------------------

def report_results(username, message1, message2):                                                                                                                                  
	
    html_code = flask.render_template('reportresults.html',
        username=username, message1=message1,message2=message2)
    response = flask.make_response(html_code)
    return response

# ----------------------------------------------------------------------

@app.route('/searchresults', methods=['GET'])
def search_results():

    title = flask.request.args.get('title')

    users = database.getData(False) # Exception handling omitted                                                                                                                                   

    html_code = flask.render_template('searchresults.html',
        title=title,
        posts=users)
    response = flask.make_response(html_code)
    return response

# ----------------------------------------------------------------------
@app.route('/home', methods=['GET'])
def homeTemplate():
	title = flask.request.form.get('title')
	body = flask.request.form.get('body')
	tag = flask.request.form.get('tag')
	posts =  database.getData(True)
	html = flask.render_template('home.html', posts=posts, title=title, body=body,tag=tag)

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
	title = flask.request.args.get('title')
	post = flask.request.args.get('post')
	print(title)
	print(post)

	html_code = flask.render_template('makeApost.html')
	response = make_response(html_code)
	return response

@app.route('/addpost', methods=['GET'])
def addPost():
	title = flask.request.form.get('title')
	body = flask.request.form.get('body')
	tag = flask.request.form.get('tag')

	database.insertData(title, body, tag)

@app.route('/beauty', methods=['GET'])
def beautyTemplate():
	posts = database.getData('beauty')
	html = flask.render_template('beautypage.html', posts=posts)

	response = make_response(html)
	return response
#-----------------------------------------------------------------------

@app.route('/events', methods=['GET'])
def eventsTemplate():
	posts = database.getData('events')
	html = flask.render_template('eventspage.html', posts=posts)

	response = make_response(html)
	return response
	
#-----------------------------------------------------------------------

@app.route('/food', methods=['GET'])
def foodTemplate():
	posts = database.getData('food')
	html = flask.render_template('foodpage.html', posts=posts)

	response = make_response(html)
	return response

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
