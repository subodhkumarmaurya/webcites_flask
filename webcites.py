#################################################################
### This python file will search for an ADS bibcode and return the [lat,long] of the author's institutes 
### then plot these on a map 
##################################################################

from __future__ import print_function, division, unicode_literals
import numpy as np
from ads_info import papersearch
from geocode import geocode

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

import os
token = os.environ.get('ADS_DEV_KEY', None)
if token:
	ads.config.token = token

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/locations/<bibcode>/', methods=["GET", "POST"])
def hello_world(bibcode):
	print("starting api-ing ads...")
	print(bibcode)
	paper_fai, paper_ai, cite_fai, cite_ai = papersearch(str(bibcode))
	print(paper_fai)
	paper_fai_loc = []
	for inst in paper_fai:
		geo = geocode(inst)
		print(geo)
		if geo:
			paper_fai_loc.append(geo)
	print('first author institutions', paper_fai_loc)
	paper_ai_loc = []
	for inst in paper_ai:
		geo = geocode(inst)
		if geo:
			paper_ai_loc.append(geo)
	print('co-author institutions', paper_ai_loc)
	cite_fai_loc = []
	for inst in cite_fai:
		geo = geocode(inst)
		if geo:
			cite_fai_loc.append(geo)
	print('citation first author institutions', cite_fai_loc)
	cite_ai_loc =[]
	for inst in cite_ai:
		geo = geocode(inst)
		if geo:
			cite_ai_loc.append(geo)
	print('citation coauthor institutions', cite_ai_loc)
	# #return "Hello world"
	# #'coauthors':paper_ai, 'citation_first_author':cite_fai, 'citation_coauthors':cite_ai})
	# #return jsonify({'coords':[51.75952470000001, -1.2584172], 'coa_coords':[[47.3768866, 8.541694], [32.8797081, -117.2350537],[44.975331, -93.23461309999999]]})
	# print('response', jsonify({'coords':paper_fai_loc, 'cao_coords':paper_ai_loc}))
	return jsonify({'coords':paper_fai_loc, 'cao_coords':paper_ai_loc, 'cite_fa':cite_fai_loc, 'cite_co': cite_ai_loc})
	#return jsonify({"cao_coords":[[51.75973,-1.259517],[51.75973,-1.259517],[47.41023,8.5084199],[51.75973,-1.259517],[52.938779,-1.201272],[51.752886,-0.242185],[50.797696,-1.098245],[50.797696,-1.098245],[50.797696,-1.098245]],"cite_co":[[38.01428985595703,-78.6001205444336],[46.63727951049805,2.3382623195648193],[-33.92481,18.64433],[-37.799502,144.968674]],"cite_fa":[[51.752886,-0.242185]],"coords":[[51.75973,-1.259517]]})


if __name__ == '__main__':
    app.run()
