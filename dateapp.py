from flask import Flask, request, abort
import datetime
import pytz


app = Flask(__name__)
@app.route('/datetime')
def get_current_datetime():
    timezone = request.args.get('timezone', 'UTC')
    if timezone not in pytz.all_timezones:
        abort(406, description=f'Timezone "{timezone}" not found.')
    else:
        tz = pytz.timezone(timezone)
        current_time = datetime.datetime.now(tz=tz)
        return f'Current datetime in {timezone} timezone: {current_time}'

@app.route("/datetimestart")
def datetime_info():
    return "This route returns the current datetime. To use it, append the timezone parameter to the URL. Example: /datetime?tz=Europe/Kiev"

@app.route("/datetime/")
def get_current_datetime_by_timezone():
    tz_name = request.args.get('tz', 'EET')
    current_datetime = datetime.datetime.now()
    return "Current datetime in {} timezone: {}".format(tz_name, current_datetime)

if __name__ == '__main__':
    app.run(host='127.0.0.3', port=5002,debug=True)