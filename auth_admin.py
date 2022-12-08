#!/usr/bin/env python

#-----------------------------------------------------------------------
# auth.py
# Authors: Alex Halderman, Scott Karlin, Brian Kernighan, Bob Dondero
#-----------------------------------------------------------------------


import database
import flask
import werkzeug.security
# from werkzeug.security import generate_password_hash


#-----------------------------------------------------------------------

def _valid_username_and_password(username, password):

    stored_password = database.get_password(username)
    # print(stored_password)
    # print(generate_password_hash('xxx'))
    if stored_password is None:
        return False
    return werkzeug.security.check_password_hash(
    stored_password, password)

#-----------------------------------------------------------------------

def login():
    error_msg = flask.request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    html = flask.render_template('login.html',
    error_msg=error_msg)
    response = flask.make_response(html)
    return response

#-----------------------------------------------------------------------

def handle_login():

    username = flask.request.form.get('admin_username')
    password = flask.request.form.get('admin_password')
    print(username)
    print(password)
    if username is None:
        return flask.redirect(
        flask.url_for('adminlogin', error_msg='Invalid login'))
    if password is None:
        return flask.redirect(
        flask.url_for('adminlogin', error_msg='Invalid login'))
    
    if not _valid_username_and_password(username, password):
        return flask.redirect(
        flask.url_for('adminlogin', error_msg='Invalid login'))
    original_url = flask.session.get('original_url', '/delete')
    response = flask.redirect(original_url)
    flask.session['admin_username'] = username
    return response

#-----------------------------------------------------------------------

def logout():
    flask.session.clear()
    html_code = flask.render_template('loggedout.html')
    response = flask.make_response(html_code)
    return response

#-----------------------------------------------------------------------

def authenticate():
    username = flask.session.get('admin_username')
    # print(username)
    if username is None:
        response = flask.redirect(flask.url_for('adminlogin'))
        flask.session['original_url'] = flask.request.url
        flask.abort(response)
    return username