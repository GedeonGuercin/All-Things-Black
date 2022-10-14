#!/usr/bin/env python

#-----------------------------------------------------------------------
# AllThingsBlack.py
# Author: Gedeon
#-----------------------------------------------------------------------

import os
import time
from flask import Flask, request, make_response, redirect, url_for
import database
import auth

#-----------------------------------------------------------------------


app = flask.Flask(__name__, template_folder='.')

app.secret_key = os.environ['APP_SECRET_KEY']




# ----------------------------------------------------------------------

@app.route('/profilePage', methods=['GET', 'POST'])
def profilePageTemplate():
	username = auth().authenticate()
	username = username.strip()
	listingID = request.args.get('list')
	sellerID = request.args.get('sellerId')
	bidder = request.args.get('bidder')
	title = request.args.get('title')
	highestBid = request.args.get('cost')
#-----------------------------------------------------------------------

# Routes for authentication.

@app.route('/logoutapp', methods=['GET'])
def logoutapp():
    return auth.logoutapp()

@app.route('/logoutcas', methods=['GET'])
def logoutcas():
    return auth.logoutcas()