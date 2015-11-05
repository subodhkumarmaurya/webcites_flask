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

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/locations/<bibcode>/', methods=["GET", "POST"])
def hello_world(bibcode):
	#bibcode = raw_input('What is the bibcode of the paper you would like to see the citation web for? :')
	print("starting api-ing ads...")
	print(bibcode)
	paper_fai, paper_ai, cite_fai, cite_ai = papersearch(str(bibcode))
	# paper_fai_loc = []
	# for inst in paper_fai:
	# 	paper_fai_loc.append(geocode(inst))
	# paper_fai_loc = [x for x in paper_fai_loc if x is not None]
	# print('first author institutions', paper_fai_loc)
	# paper_ai_loc = []
	# for inst in paper_ai:
	# 	paper_ai_loc.append(geocode(inst))
	# paper_ai_loc = [x for x in paper_ai_loc if x is not None]
	# print('co-author institutions', paper_ai_loc)
	# cite_fai_loc = []
	# for inst in cite_fai:
	# 	cite_fai_loc.append(geocode(inst))
	# cite_fai_loc = [x for x in cite_fai_loc if x is not None]
	# print('citation first author institutions', cite_fai_loc)
	# cite_ai_loc =[]
	# for inst in cite_ai:
	# 	cite_ai_loc.append(geocode(inst))
	# cite_ai_loc = [x for x in cite_ai_loc if x is not None]
	# print('citation coauthor institutions', cite_ai_loc)
	#return "Hello world"
	#'coauthors':paper_ai, 'citation_first_author':cite_fai, 'citation_coauthors':cite_ai})
	return jsonify({'coords':[51.75952470000001, -1.2584172], 'coa_coords':[[47.3768866, 8.541694], [32.8797081, -117.2350537],[44.975331, -93.23461309999999]]})


if __name__ == '__main__':
    app.run()
