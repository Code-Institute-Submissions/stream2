from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from settings import URI, HOST, PORT, COLLECTION, DATABASE

app = Flask(__name__)


FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False, 'primary_focus_subject': True }


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_donations')
def donor_projects():
    client = MongoClient(URI)
    collection = client[DATABASE][COLLECTION]
    donations = collection.find(projection=FIELDS, limit=5000)
    donation_list = []
    for donation in donations:
        donation_list.append(donation)
    json_projects = json.dumps(donation_list)
    client.close()
    return json_projects

if __name__ == '__main__':
    app.run(debug=True, port=4000)
