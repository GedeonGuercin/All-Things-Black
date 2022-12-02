#!/usr/bin/env python

#-----------------------------------------------------------------------
# auths.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

import flask
import werkzeug.security
import database

#-----------------------------------------------------------------------

def _valid_username_and_password(username, password):

    stored_password = database.get_password(username)
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

    username = flask.request.form.get('username')
    password = flask.request.form.get('password')
    if username is None:
        return flask.redirect(
            flask.url_for('login', error_msg='Invalid login'))
    if password is None:
        return flask.redirect(
            flask.url_for('login', error_msg='Invalid login'))
    if not _valid_username_and_password(username, password):
        return flask.redirect(
            flask.url_for('login', error_msg='Invalid login'))
    original_url = flask.session.get('original_url', '/index')
    response = flask.redirect(original_url)
    flask.session['username'] = username
    return response

#-----------------------------------------------------------------------

def logout():

    flask.session.clear()
    html_code = flask.render_template('loggedout.html')
    response = flask.make_response(html_code)
    return response

#-----------------------------------------------------------------------

def authenticate():

    username = flask.session.get('username')
    if username is None:
        response = flask.redirect(flask.url_for('login'))
        flask.session['original_url'] = flask.request.url
        flask.abort(response)
    return username