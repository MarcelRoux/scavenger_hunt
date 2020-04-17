# Scavenger Hunt

This app serves as a basic scavenger hunt to search for clues, either digital or physical.

Hints are provided that lead to the next key, which in turn lead to the next set of hints until all keys have been found.

## Start app

This will start app on provided host and port.
```
SET FLASK_APP=app.py
SET FLASK_ENV=development

flask run -h 192.168.0.128 -p 80
```