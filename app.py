from flask import Flask, Response, render_template

from data.data import get_data, shuffle_hints

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404


@app.route('/')
def welcome_to_trial():
    return render_template('index.html')

@app.route('/<key>')
def egg(key):
    data = get_data()
    if(key in data):
        datum = data[key]
        egg_no = datum['egg_number']
        hints = shuffle_hints(datum['hints'])

        return render_template('egg.html', egg_no=egg_no, hints=hints)
    
    else:
        return render_template('404.html', title = '404'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()
