#!/usr/bin/env python

#-----------------------------------------------------------------------
# AllThingsBlack.py
# Author: Gedeon
#-----------------------------------------------------------------------

import flask
from flask import make_response
import database
import auth
import auth_admin

#-----------------------------------------------------------------------

app = flask.Flask(__name__, template_folder='.')
app.secret_key = '93c4828df59a50ae7ea98bbb'
#app.secret_key = os.getenv('SOME_VAR')

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
# Route for the home page.

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    username = auth.authenticate() 
    html_code = flask.render_template('index.html', username=username)
    response = flask.make_response(html_code)
    return response

#-----------------------------------------------------------------------
# Route for the delete page.

@app.route('/delete', methods=['GET'])
def delete():
	username = auth_admin.authenticate()
	posts =  database.getData(True)

	html_code = flask.render_template('delete.html', username=username, posts=posts)
	response = flask.make_response(html_code)
	return response
	

#-----------------------------------------------------------------------
# Route for error messages on the delete page

@app.route('/deleteresults', methods=['POST'])
def deleteresult():
	username = auth_admin.authenticate()
	title  = flask.request.form.get('title')
	title = title.strip()
	print(title)
	database.delete_post(title)

	message1 = 'The deletion done by ' + username+ ' was successful'
	message2 = 'The database now does not contain a post with Title '
	message2 += title

	return report_results(username, message1, message2)
	
#-----------------------------------------------------------------------
# Function to generate the reportresults.html page that reports the 
# results when a deletion occurs.

def report_results(username, message1, message2):                                                                                                                                  
	
    html_code = flask.render_template('reportresults.html',
        username=username, message1=message1,message2=message2)
    response = flask.make_response(html_code)
    return response

# ----------------------------------------------------------------------
# Route for the page with all posts

@app.route('/all', methods=['GET'])
def allTemplate():
	username = auth.authenticate() 
	title = flask.request.form.get('title')
	body = flask.request.form.get('body')
	tag = flask.request.form.get('tag')
	posts =  database.getData(True)
	html = flask.render_template('all.html', 
	posts=posts, title=title, body=body,tag=tag,username=username)

	response = make_response(html)
	return response

#-----------------------------------------------------------------------
# Route for the page with information about us.

@app.route('/aboutUs', methods=['GET'])
def aboutUsTemplate():
	username = auth.authenticate() 
	html = flask.render_template('aboutUs.html',username=username)

	response = make_response(html)
	return response

#-----------------------------------------------------------------------
# Route for the page to add a post.

@app.route('/post', methods=['GET'])
def makeaPost():
	username = auth.authenticate() 
	title = flask.request.args.get('title')
	post = flask.request.args.get('post')
	print(title)
	print(post)

	html_code = flask.render_template('makeApost.html',username=username)
	response = make_response(html_code)
	return response

#-----------------------------------------------------------------------
# Route for the beauty page.

@app.route('/beauty', methods=['GET'])
def beautyTemplate():
	username = auth.authenticate() 
	posts = database.getData('beauty')
	html = flask.render_template('beautypage.html', posts=posts,username=username)

	response = make_response(html)
	return response
#-----------------------------------------------------------------------
# Route for the events page.

@app.route('/events', methods=['GET'])
def eventsTemplate():
	username = auth.authenticate() 
	posts = database.getData('events')
	html = flask.render_template('eventspage.html', posts=posts,username=username)

	response = make_response(html)
	return response
	
#-----------------------------------------------------------------------
# Route for the food page.

@app.route('/food', methods=['GET'])
def foodTemplate():
	username = auth.authenticate() 
	posts = database.getData('food')
	html = flask.render_template('foodpage.html', posts=posts,username=username)

	response = make_response(html)
	return response

#-----------------------------------------------------------------------
# Route to add user input to pages

@app.route('/addresults', methods=['POST'])
def add_results():
	title = flask.request.form.get('title')
	body = flask.request.form.get('body')
	tag = flask.request.form.get('tag')

	print(title)
	print(body)
	print(tag)

	database.addPost(title, body, tag)
	
	return allTemplate()
