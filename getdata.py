"""
	This script uses Northwestern University's course API to gather information about offered courses.The API is structured in a way that certain queries can only be made with a minimum number of parameters. Thus, the process for arriving at a JSON file with all the courses offered in one term is as follows:

		1) Retrieve list of all terms.
		2) Retrieve unique ID of latest term available.
		3) Use unique ID of term to retrive list of all subjects for which courses are being offered for that term.
		4) Retrieve subject ID for each of those subjects.
		5) Use unique ID of term and subject ID to retrieve list of all courses offered for each subject being offered in that term. 

"""
import requests
from urlparse import urljoin

API_KEY="1kekecMN31fxge0j"
BASE_URL="http://api.asg.northwestern.edu/"

def api_call(url_path, **params): # function to get api response with specified parameters
	params["key"]=API_KEY
	response=requests.get(urljoin(BASE_URL,url_path), params=params)
	return response.json()

def terms(): 
	return api_call("terms")

def subjects(term_id):
	return api_call("subjects", term=term_id)

def courses(term_id, subject_code):
	return api_call("courses", subject=subject_code, term=term_id)	

all_terms=list(reversed((sorted(terms(), key=lambda x: x["start_date"])))) # sort the json of all terms by their start date, reverse the order so most recent appears earliest, turn into list

latest_term_id=all_terms[0]["id"] # get unique id of the latest term
all_subjects=subjects(latest_term_id) # get json of all subjects offered for the latest term

subject_codes=[] # create a list of all the subject codes
for subject in all_subjects:
	subject_codes.append(subject["symbol"])

for subject_code in subject_codes: # produce json of all courses offered in the latest term
	f=open('courses.json', 'a')
	print >> f, courses(latest_term_id, subject_code)



