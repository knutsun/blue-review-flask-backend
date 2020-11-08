from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL
from flask_cors import CORS
import simplejson as json

app = Flask(__name__)
CORS(app)


# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123god1;'
app.config['MYSQL_DB'] = 'officers'

mysql = MySQL(app)

def conn():
    # Creating a connection cursor
    cur = mysql.connection.cursor()
    return cur


def get_police_demographic_by_race(race):
    # Creating a connection cursor
    cur = conn()

    # Executing SQL Statements
    cur.execute("SELECT departmentcitydemographics{} FROM nyc_schema".format(race))

    # Saving the Actions performed on the DB
    mysql.connection.commit()

    departments = cur.fetchone()
    # output = json.dumps(departments)

    # Closing the cursor
    cur.close()

    return departments


@app.route('/departments/', methods=["GET"])
def get_departments():

    # departments = get_police_demographic_by_race("black")
    # print(departments)

    data = ({
        "department": {
            "city": {
                "name": "New York City",
                "white": get_police_demographic_by_race("white")[0],
                "hispanic": get_police_demographic_by_race("hispanic")[0],
                "black": get_police_demographic_by_race("black")[0],
                "asian": get_police_demographic_by_race("asian")[0],
                "nativeAmerican": get_police_demographic_by_race("nativeAmerican")[0],
                "biracial": get_police_demographic_by_race("biracial")[0],
            }
        }
    })

    # data = ({
    #     "department": {
    #         "image": "./static/img/departments/newyorkcityny.jpg",
    #         "address": "1 Police Plaza",
    #         "city": {
    #             "name": get_department_city(),
    #             "population": 8398748,
    #             "demographics": {
    #                 "white": 32.1,
    #                 "nativeAmerican": 0.4,
    #                 "black": 24.3,
    #                 "hispanic": 29.1,
    #                 "asian": 13.9,
    #                 "biracial": None,
    #                 "raceSource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
    #                 "raceSourceLastUpdated": "20201026",
    #             },
    #         },
    #         "demographics": {
    #             "female": 19,
    #             "male": 81,
    #             "genderSource": "https://www1.nyc.gov/site/ccrb/policy/<br />data-transparency-initiative-mos.page",
    #             "white": 46.7,
    #             "nativeAmerican": 0.1,
    #             "black": 15.2,
    #             "hispanic": 29.1,
    #             "asian": 8.9,
    #             "biracial": None,
    #             "raceSource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
    #             "raceSourceLastUpdated": "20201026",
    #         },
    #
    #         "state": "New York",
    #         "acronymn": "NYPD",
    #         "yearFounded": 1845,
    #         "commissioner": "Dermot F. Shea",
    #         "url": "https://www1.nyc.gov/site/nypd/index.page",
    #         "twitterUrl": "https://twitter.com/NYPDnews",
    #         "twitterHandle": "NYPDnews",
    #         "commissionerYearStarted": 2019,
    #     },
    # },
    # {
    #     "department": {
    #         "image": "./static/img/departments/chicagoil.jpg",
    #         "address": "3510 S. Michigan Ave",
    #         "city": {
    #             "name": "Chicago",
    #             "population": 2705994,
    #             "demographics": {
    #                 "white": 32.1,
    #                 "nativeAmerican": 0.4,
    #                 "black": 24.3,
    #                 "hispanic": 29.1,
    #                 "asian": 13.9,
    #                 "biracial": None,
    #                 "raceSource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
    #                 "raceSourceLastUpdated": "20201026",
    #             },
    #         },
    #         "demographics": {
    #             "female": 22.38,
    #             "male": 77.62,
    #             "genderSource": "https://home.chicagopolice.org/wp-content/uploads/2019/03/Chicago-Police-Department-Annual-Report-2017.pdf",
    #             "white": 50.1,
    #             "nativeAmerican": 0.31,
    #             "black": 20.93,
    #             "hispanic": 24.93,
    #             "asian": 3.11,
    #             "biracial": None,
    #             "raceSource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
    #             "raceSourceLastUpdated": "20201026",
    #         },
    #         "state": "Illinois",
    #         "acronymn": "CPD",
    #         "yearFounded": 1835,
    #         "commissioner": "David Brown",
    #         "url": "https://home.chicagopolice.org/",
    #         "twitterUrl": "https://twitter.com/Chicago_Police",
    #         "twitterHandle": "Chicago_Police",
    #         "commissionerYearStarted": 2020,
    #     },
    #
    # })

    response = make_response(jsonify(response=data))

    # Enable Access-Control-Allow-Origin
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.mimetype = 'application/json'

    print("Call to /departments:", response.status_code, '\n')
    print("Response is:", response.status_code)
    print(response.data)
    return response


@app.route('/departments/overview', methods=["GET"])
def get_departments_overview():
    pass
    # response = make_response(jsonify(response=data))
    #
    # # Enable Access-Control-Allow-Origin
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.mimetype = 'application/json'
    # return response


if __name__ == '__main__':
    app.run(debug=True)
