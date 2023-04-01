from flask import Flask, request
import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def get_current_datetime():
    tz_name = request.args.get('tz', '')
    try:
        tz = pytz.timezone(tz_name)
        now = datetime.datetime.now()
        return f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}"
    except pytz.exceptions.UnknownTimeZoneError:
        return "Invalid timezone: {}".format(tz_name)

@app.route('/+2')
def get_datetime():
    tz_name = request.args.get('tz', '')
    try:
        gmt2 = pytz.timezone('EET')
        current_time = datetime.datetime.now(gmt2)
        return f"The current date and time in GMT+2 is {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
    except pytz.exceptions.UnknownTimeZoneError:
        return "Invalid timezone: {}".format(tz_name)

@app.route('/0')
def get_datetime_for0():
    tz_name = request.args.get('tz', '')
    try:
        gmt = pytz.timezone('GMT')
        current_time = datetime.datetime.now(gmt)
        return f"The current date and time in GMT0 is {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
    except pytz.exceptions.UnknownTimeZoneError:
        return "Invalid timezone: {}".format(tz_name)




if __name__ == '__main__':
    app.run(host='127.0.0.2', port=5001,debug=True)
