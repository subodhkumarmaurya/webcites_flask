#################################################################
### This python file will use the ADS API written by Andy Casey: https://github.com/andycasey/ads to search the ADS for
### a given paper and find the author's institutes and the institutes of the authors of the papers which cited the 
### searched for paper. From these institute names the program finds the geolocation in [lat, long] of each of these
### institutions by scraping from google maps.  
##################################################################
from __future__ import print_function, division, unicode_literals
import numpy as np
import ads


def papersearch(search_bibcode):
	"""
	Function when given a bibcode of paper will return the first author's institude, a list of the co-author institutions
	and lists of both the first author and coauthor institutions of papers that have cited the given paper. 
	"""
	paper = list(ads.SearchQuery(bibcode=str(search_bibcode)))
	if len(paper)==0:
		print('Sorry, that paper was not found. Please ensure you are entering a bibcode, e.g. "2015MNRAS.451.2933B"')
		raise SystemExit()
	elif len(paper) > 1:
		n =0
		for pap in paper:
			n+=1
			print(n, ':', pap.title)
		corr_paper = float(raw_input('There were a few possible options for your search, please choose the paper you meant by selecting the correct number: '))
		paper = paper[corr_paper-1]
	else:
		pass

	paper_fai = paper[0].aff[0].split(';') 
	paper_ai = [i.split(';') for i in paper[0].aff[1:]]

	citations = paper[0].citation
	cite_fai =[]
	cite_ai = []

	for cit in citations: 
		cit_search = list(ads.SearchQuery(bibcode=str(cit)))
		if len(cit_search)==0:
			pass
		elif len(cit_search) > 0:
			cite = cit_search[0]
		else:
			cite = cit_search 
		cite_fai.extend(cite.aff[0].split(';'))
		cite_ai.extend([i.split(';') for i in cite.aff[1:]])
	n =0
	for item in paper_fai:
		if type(item) != unicode:
				n+=1
		else:
			pass
	if n > 0:
		paper_fai = [item for sublist in paper_fai for item in sublist]
	else:
		pass
	n =0
	for item in paper_ai:
		if type(item) != unicode:
				n+=1
		else:
			pass
	if n > 0:
		paper_ai = [item for sublist in paper_ai for item in sublist]
	else:
		pass
	n =0
	for item in cite_fai:
		if type(item) != unicode:
				n+=1
		else:
			pass
	if n > 0:
		cite_fai = [item for sublist in cite_fai for item in sublist]
	else:
		pass
	n =0
	for item in cite_ai:
		if type(item) != unicode:
				n+=1
		else:
			pass
	if n > 0:
		cite_ai = [item for sublist in cite_ai for item in sublist]
	else:
		pass

	return paper_fai, paper_ai, cite_fai, cite_ai


