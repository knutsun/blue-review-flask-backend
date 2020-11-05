from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123god1;'
app.config['MYSQL_DB'] = 'officers'

mysql = MySQL(app)


@app.route('/departments/', methods=["GET"])
def get_departments():

    data = ({
        "city": "New York City, New York",
        "image": "./static/img/departments/newyorkcityny.jpg",
        "policeFemale": 19,
        "policeMale": 81,
        "genderSource": "https://www1.nyc.gov/site/ccrb/policy/<br />data-transparency-initiative-mos.page",
        "racialParityIndex": 0.0,
        "whiteParityIndex": 0.0,
        "nativeAmericanParityIndex": 0.0,
        "blackParityIndex": 0.0,
        "hispanicParityIndex": 0.0,
        "asianParityIndex": 0.0,
        "policeWhite": 46.7,
        "policeNativeAmerican": 0.1,
        "policeBlack": 15.2,
        "policeHispanic": 29.1,
        "policeAsian": 8.9,
        "policeSource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
        "policeSourceLastUpdated": "20201026",
        "communityWhite": 32.1,
        "communityNativeAmerican": 0.4,
        "communityBlack": 24.3,
        "communityHispanic": 29.1,
        "communityAsian": 13.9,
        "communitySource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
        "communitySourceLastUpdated": "20201026",
    },
    {
        "city": "Chicago, Illinois",
        "image": "./static/img/departments/chicagoil.jpg",
        "genderSource": "https://home.chicagopolice.org/wp-content/uploads/2019/03/Chicago-Police-Department-Annual-Report-2017.pdf",
        "policeFemale": 22.38,
        "policeMale": 77.62,
        "racialParityIndex": 0.0,
        "whiteParityIndex": 0.0,
        "nativeAmericanParityIndex": 0.0,
        "blackParityIndex": 0.0,
        "hispanicParityIndex": 0.0,
        "asianParityIndex": 0.0,
        "policeWhite": 50.1,
        "policeNativeAmerican": 0.31,
        "policeBlack": 20.93,
        "policeHispanic": 24.93,
        "policeAsian": 3.11,
        "policeSource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
        "policeSourceLastUpdated": "20201026",
        "communityWhite": 32.1,
        "communityNativeAmerican": 0.4,
        "communityBlack": 24.3,
        "communityHispanic": 29.1,
        "communityAsian": 13.9,
        "communitySource": "https://app.powerbigov.us/view?r=eyJrIjoiZTI4OTRjZTYtNTYwOC00NzcxLThhYTItOTU5NGNkMzIzYjVlIiwidCI6IjJiOWY1N2ViLTc4ZDEtNDZmYi1iZTgzLWEyYWZkZDdjNjA0MyJ9&pageName=ReportSection",
        "communitySourceLastUpdated": "20201026",
    })

    response = make_response(jsonify(response=data))

    # Enable Access-Control-Allow-Origin
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.mimetype = 'application/json'


    print("Call to /departments:", response.status_code, '\n')
    print("Response is:", response.status_code)
    return response


# @app.route('/officers')
# def get_officers():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT first_name, last_name, mid_initial, locality FROM nycnyofficers''')
#     rv = cur.fetchall()

#     # f.write("[")
#     # output += json.dumps(officer.__dict__) + ","
#     # f.write(output[:-1])
#     # f.write("]")

#     return str(rv)


with app.test_client() as client:
    response = client.get('/departments')
    print(response.get_data())
    print(response)

    # the contexts are not popped even though the request ended
    print(request.url)
    print(request.host)
    print(request.path)


if __name__ == '__main__':
    app.run(debug=True)
