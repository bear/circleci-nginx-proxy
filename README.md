A test Python Flask app to show how to have Nginx act as a proxy-forward inside of a CircleCI build.

## Requirements and Assumptions
- Python v2.7
- Nginx

## Configuration


## Installation



## Running
```
FLASK_SETTINGS=./foob/settings.py uwsgi --socket 127.0.0.1:5000 --module service --callable application
```
