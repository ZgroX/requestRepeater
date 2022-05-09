import datetime
import time

from flask import Flask, request, send_file
import requests as req

app = Flask(__name__)


@app.route('/filesignature', methods=['GET', 'POST'])
def request_repeater():  # put application's code here
    if request.method == 'POST':
        json = request.get_json()
        try:
            start_date = datetime.datetime.strptime(json["start"], "%Y-%m-%d %H:%M:%S")
        except:
            start_date = datetime.datetime.now()
        end_date = datetime.datetime.strptime(json["end"], "%Y-%m-%d %H:%M:%S")
        link = json["link"]
        try:
            ratio = json["ratio"]
        except:
            ratio = 0
        try:
            file_size = json["file_size"]
        except:
            file_size = 1

        request_sender(start_date, end_date, ratio, link, f'example{file_size}.pdf')

    return 'Done'



def request_sender(start, stop, ratio, link, file):
    while datetime.datetime.now() < stop:
        if start < datetime.datetime.now():
            req.post(link, files={'pdf': open(file, 'rb')})
            if ratio != 0:
                time.sleep(60/ratio)
        else:
            time.sleep(60)

if __name__ == '__main__':
    app.run(threaded=True)
